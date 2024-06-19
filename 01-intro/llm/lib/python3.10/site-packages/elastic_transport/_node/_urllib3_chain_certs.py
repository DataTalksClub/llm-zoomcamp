#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import hashlib
import sys
from binascii import hexlify, unhexlify
from hmac import compare_digest
from typing import Any, List, Optional

import _ssl  # type: ignore
import urllib3
import urllib3.connection

from ._base import RERAISE_EXCEPTIONS

if sys.version_info < (3, 10) or sys.implementation.name != "cpython":
    raise ImportError("Only supported on CPython 3.10+")

_ENCODING_DER: int = _ssl.ENCODING_DER
_HASHES_BY_LENGTH = {32: hashlib.md5, 40: hashlib.sha1, 64: hashlib.sha256}

__all__ = ["HTTPSConnectionPool"]


class HTTPSConnection(urllib3.connection.HTTPSConnection):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._elastic_assert_fingerprint: Optional[str] = None
        super().__init__(*args, **kwargs)

    def connect(self) -> None:
        super().connect()
        # Hack to prevent a warning within HTTPSConnectionPool._validate_conn()
        if self._elastic_assert_fingerprint:
            self.is_verified = True


class HTTPSConnectionPool(urllib3.HTTPSConnectionPool):
    ConnectionCls = HTTPSConnection

    """HTTPSConnectionPool implementation which supports ``assert_fingerprint``
    on certificates within the chain instead of only the leaf cert using private
    APIs in CPython 3.10+
    """

    def __init__(
        self, *args: Any, assert_fingerprint: Optional[str] = None, **kwargs: Any
    ) -> None:
        self._elastic_assert_fingerprint = (
            assert_fingerprint.replace(":", "").lower() if assert_fingerprint else None
        )

        # Complain about fingerprint length earlier than urllib3 does.
        if (
            self._elastic_assert_fingerprint
            and len(self._elastic_assert_fingerprint) not in _HASHES_BY_LENGTH
        ):
            valid_lengths = "', '".join(map(str, sorted(_HASHES_BY_LENGTH.keys())))
            raise ValueError(
                f"Fingerprint of invalid length '{len(self._elastic_assert_fingerprint)}'"
                f", should be one of '{valid_lengths}'"
            )

        if self._elastic_assert_fingerprint:
            # Skip fingerprinting by urllib3 as we'll do it ourselves
            kwargs["assert_fingerprint"] = None

        super().__init__(*args, **kwargs)

    def _new_conn(self) -> HTTPSConnection:
        """
        Return a fresh :class:`urllib3.connection.HTTPSConnection`.
        """
        conn: HTTPSConnection = super()._new_conn()  # type: ignore[assignment]
        # Tell our custom connection if we'll assert fingerprint ourselves
        conn._elastic_assert_fingerprint = self._elastic_assert_fingerprint
        return conn

    def _validate_conn(self, conn: HTTPSConnection) -> None:  # type: ignore[override]
        """
        Called right before a request is made, after the socket is created.
        """
        super(HTTPSConnectionPool, self)._validate_conn(conn)

        if self._elastic_assert_fingerprint:
            hash_func = _HASHES_BY_LENGTH[len(self._elastic_assert_fingerprint)]
            assert_fingerprint = unhexlify(
                self._elastic_assert_fingerprint.lower()
                .replace(":", "")
                .encode("ascii")
            )

            fingerprints: List[bytes]
            try:
                # 'get_verified_chain()' and 'Certificate.public_bytes()' are private APIs
                # in CPython 3.10. They're not documented anywhere yet but seem to work
                # and we need them for Security on by Default so... onwards we go!
                # See: https://github.com/python/cpython/pull/25467
                fingerprints = [
                    hash_func(cert.public_bytes(_ENCODING_DER)).digest()
                    for cert in conn.sock._sslobj.get_verified_chain()  # type: ignore[union-attr]
                ]
            except RERAISE_EXCEPTIONS:  # pragma: nocover
                raise
            # Because these are private APIs we are super careful here
            # so that if anything "goes wrong" we fallback on the old behavior.
            except Exception:  # pragma: nocover
                fingerprints = []

            # Only add the peercert in front of the chain if it's not there for some reason.
            # This is to make sure old behavior of 'ssl_assert_fingerprint' still works.
            peercert_fingerprint = hash_func(conn.sock.getpeercert(True)).digest()  # type: ignore[union-attr]
            if peercert_fingerprint not in fingerprints:  # pragma: nocover
                fingerprints.insert(0, peercert_fingerprint)

            # If any match then that's a success! We always run them
            # all through though because of constant time concerns.
            success = False
            for fingerprint in fingerprints:
                success |= compare_digest(fingerprint, assert_fingerprint)

            # Give users all the fingerprints we checked against in
            # order of peer -> root CA.
            if not success:
                raise urllib3.exceptions.SSLError(
                    'Fingerprints did not match. Expected "{0}", got "{1}".'.format(
                        self._elastic_assert_fingerprint,
                        '", "'.join([x.decode() for x in map(hexlify, fingerprints)]),
                    )
                )
            conn.is_verified = success
