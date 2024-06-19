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
from typing import Tuple, Type, Union

string_types: Tuple[Type[str], Type[bytes]] = (str, bytes)


def to_str(x: Union[str, bytes], encoding: str = "ascii") -> str:
    if not isinstance(x, str):
        return x.decode(encoding)
    return x


def to_bytes(x: Union[str, bytes], encoding: str = "ascii") -> bytes:
    if not isinstance(x, bytes):
        return x.encode(encoding)
    return x


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
    "string_types",
    "to_str",
    "to_bytes",
    "warn_stacklevel",
]
