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

import re
from typing import Any, Dict, Union


def fixup_module_metadata(module_name: str, namespace: Dict[str, Any]) -> None:
    # Yoinked from python-trio/outcome, thanks Nathaniel! License: MIT
    def fix_one(obj: Any) -> None:
        mod = getattr(obj, "__module__", None)
        if mod is not None and mod.startswith("elastic_transport."):
            obj.__module__ = module_name
            if isinstance(obj, type):
                for attr_value in obj.__dict__.values():
                    fix_one(attr_value)

    for objname in namespace["__all__"]:
        obj = namespace[objname]
        fix_one(obj)


IPV4_PAT = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
IPV4_RE = re.compile("^" + IPV4_PAT + "$")

HEX_PAT = "[0-9A-Fa-f]{1,4}"
LS32_PAT = "(?:{hex}:{hex}|{ipv4})".format(hex=HEX_PAT, ipv4=IPV4_PAT)
_subs = {"hex": HEX_PAT, "ls32": LS32_PAT}
_variations = [
    #                            6( h16 ":" ) ls32
    "(?:%(hex)s:){6}%(ls32)s",
    #                       "::" 5( h16 ":" ) ls32
    "::(?:%(hex)s:){5}%(ls32)s",
    # [               h16 ] "::" 4( h16 ":" ) ls32
    "(?:%(hex)s)?::(?:%(hex)s:){4}%(ls32)s",
    # [ *1( h16 ":" ) h16 ] "::" 3( h16 ":" ) ls32
    "(?:(?:%(hex)s:)?%(hex)s)?::(?:%(hex)s:){3}%(ls32)s",
    # [ *2( h16 ":" ) h16 ] "::" 2( h16 ":" ) ls32
    "(?:(?:%(hex)s:){0,2}%(hex)s)?::(?:%(hex)s:){2}%(ls32)s",
    # [ *3( h16 ":" ) h16 ] "::"    h16 ":"   ls32
    "(?:(?:%(hex)s:){0,3}%(hex)s)?::%(hex)s:%(ls32)s",
    # [ *4( h16 ":" ) h16 ] "::"              ls32
    "(?:(?:%(hex)s:){0,4}%(hex)s)?::%(ls32)s",
    # [ *5( h16 ":" ) h16 ] "::"              h16
    "(?:(?:%(hex)s:){0,5}%(hex)s)?::%(hex)s",
    # [ *6( h16 ":" ) h16 ] "::"
    "(?:(?:%(hex)s:){0,6}%(hex)s)?::",
]
IPV6_PAT = "(?:" + "|".join([x % _subs for x in _variations]) + ")"
UNRESERVED_PAT = r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._!\-~"
ZONE_ID_PAT = "(?:%25|%)(?:[" + UNRESERVED_PAT + "]|%[a-fA-F0-9]{2})+"
BRACELESS_IPV6_ADDRZ_PAT = IPV6_PAT + r"(?:" + ZONE_ID_PAT + r")?"
BRACELESS_IPV6_ADDRZ_RE = re.compile("^" + BRACELESS_IPV6_ADDRZ_PAT + "$")


def is_ipaddress(hostname: Union[str, bytes]) -> bool:
    """Detects whether the hostname given is an IPv4 or IPv6 address.
    Also detects IPv6 addresses with Zone IDs.
    """
    # Copied from urllib3. License: MIT
    if isinstance(hostname, bytes):
        # IDN A-label bytes are ASCII compatible.
        hostname = hostname.decode("ascii")
    hostname = hostname.strip("[]")
    return bool(IPV4_RE.match(hostname) or BRACELESS_IPV6_ADDRZ_RE.match(hostname))
