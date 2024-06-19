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

import inspect
import sys
from pathlib import Path
from typing import Any, Awaitable, TypeVar, Union
from urllib.parse import quote as _quote
from urllib.parse import urlencode, urlparse

string_types = (str, bytes)

if sys.version_info >= (3, 7):  # dict is insert ordered on Python 3.7+
    ordered_dict = dict
else:
    from collections import OrderedDict as ordered_dict


T = TypeVar("T")


async def await_if_coro(coro: Union[T, Awaitable[T]]) -> T:
    if inspect.iscoroutine(coro):
        return await coro  # type: ignore
    return coro  # type: ignore


_QUOTE_ALWAYS_SAFE = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-~"
)


def quote(string: str, safe: str = "/") -> str:
    # Redefines 'urllib.parse.quote()' to always have the '~' character
    # within the 'ALWAYS_SAFE' list. The character was added in Python 3.7
    safe = "".join(_QUOTE_ALWAYS_SAFE.union(set(safe)))
    return _quote(string, safe)


try:
    from threading import Lock
except ImportError:

    class Lock:  # type: ignore
        def __enter__(self) -> None:
            pass

        def __exit__(self, *_: Any) -> None:
            pass

        def acquire(self, _: bool = True) -> bool:
            return True

        def release(self) -> None:
            pass


def warn_stacklevel() -> int:
    """Dynamically determine warning stacklevel for warnings based on the call stack"""
    try:
        # Grab the root module from the current module '__name__'
        module_name = __name__.partition(".")[0]
        module_path = Path(sys.modules[module_name].__file__)  # type: ignore[arg-type]

        # If the module is a folder we're looking at
        # subdirectories, otherwise we're looking for
        # an exact match.
        module_is_folder = module_path.name == "__init__.py"
        if module_is_folder:
            module_path = module_path.parent

        # Look through frames until we find a file that
        # isn't a part of our module, then return that stacklevel.
        for level, frame in enumerate(inspect.stack()):
            # Garbage collecting frames
            frame_filename = Path(frame.filename)
            del frame

            if (
                # If the module is a folder we look at subdirectory
                module_is_folder
                and module_path not in frame_filename.parents
            ) or (
                # Otherwise we're looking for an exact match.
                not module_is_folder
                and module_path != frame_filename
            ):
                return level
    except KeyError:
        pass
    return 0


__all__ = [
    "await_if_coro",
    "ordered_dict",
    "quote",
    "urlparse",
    "urlencode",
    "string_types",
    "Lock",
]
