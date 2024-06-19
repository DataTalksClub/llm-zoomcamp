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

from typing import (
    Any,
    Dict,
    Generic,
    Iterator,
    List,
    NoReturn,
    Tuple,
    TypeVar,
    Union,
    overload,
)

from ._models import ApiResponseMeta

_BodyType = TypeVar("_BodyType")
_ObjectBodyType = TypeVar("_ObjectBodyType")
_ListItemBodyType = TypeVar("_ListItemBodyType")


class ApiResponse(Generic[_BodyType]):
    """Base class for all API response classes"""

    __slots__ = ("_body", "_meta")

    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ):
        def _raise_typeerror() -> NoReturn:
            raise TypeError("Must pass 'meta' and 'body' to ApiResponse") from None

        # Working around pre-releases of elasticsearch-python
        # that would use raw=... instead of body=...
        try:
            if bool(args) == bool(kwargs):
                _raise_typeerror()
            elif args and len(args) == 2:
                body, meta = args
            elif kwargs and "raw" in kwargs:
                body = kwargs.pop("raw")
                meta = kwargs.pop("meta")
                kwargs.pop("body_cls", None)
            elif kwargs and "body" in kwargs:
                body = kwargs.pop("body")
                meta = kwargs.pop("meta")
                kwargs.pop("body_cls", None)
            else:
                _raise_typeerror()
        except KeyError:
            _raise_typeerror()
        # If there are still kwargs left over
        # and we're not in positional mode...
        if not args and kwargs:
            _raise_typeerror()

        self._body = body
        self._meta = meta

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.body!r})"

    def __contains__(self, item: Any) -> bool:
        return item in self._body

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ApiResponse):
            other = other.body
        return self._body == other  # type: ignore[no-any-return]

    def __ne__(self, other: object) -> bool:
        if isinstance(other, ApiResponse):
            other = other.body
        return self._body != other  # type: ignore[no-any-return]

    def __getitem__(self, item: Any) -> Any:
        return self._body[item]

    def __getattr__(self, attr: str) -> Any:
        return getattr(self._body, attr)

    def __getstate__(self) -> Tuple[_BodyType, ApiResponseMeta]:
        return self._body, self._meta

    def __setstate__(self, state: Tuple[_BodyType, ApiResponseMeta]) -> None:
        self._body, self._meta = state

    def __len__(self) -> int:
        return len(self._body)

    def __iter__(self) -> Iterator[Any]:
        return iter(self._body)

    def __str__(self) -> str:
        return str(self._body)

    def __bool__(self) -> bool:
        return bool(self._body)

    @property
    def meta(self) -> ApiResponseMeta:
        """Response metadata"""
        return self._meta  # type: ignore[no-any-return]

    @property
    def body(self) -> _BodyType:
        """User-friendly view into the raw response with type hints if applicable"""
        return self._body  # type: ignore[no-any-return]

    @property
    def raw(self) -> _BodyType:
        return self.body


class TextApiResponse(ApiResponse[str]):
    """API responses which are text such as 'text/plain' or 'text/csv'"""

    def __iter__(self) -> Iterator[str]:
        return iter(self.body)

    def __getitem__(self, item: Union[int, slice]) -> str:
        return self.body[item]

    @property
    def body(self) -> str:
        return self._body  # type: ignore[no-any-return]


class BinaryApiResponse(ApiResponse[bytes]):
    """API responses which are a binary response such as Mapbox vector tiles"""

    def __iter__(self) -> Iterator[int]:
        return iter(self.body)

    @overload
    def __getitem__(self, item: slice) -> bytes: ...

    @overload
    def __getitem__(self, item: int) -> int: ...

    def __getitem__(self, item: Union[int, slice]) -> Union[int, bytes]:
        return self.body[item]

    @property
    def body(self) -> bytes:
        return self._body  # type: ignore[no-any-return]


class HeadApiResponse(ApiResponse[bool]):
    """API responses which are for an 'exists' / HEAD API request"""

    def __init__(self, meta: ApiResponseMeta):
        super().__init__(body=200 <= meta.status < 300, meta=meta)

    def __bool__(self) -> bool:
        return 200 <= self.meta.status < 300

    @property
    def body(self) -> bool:
        return bool(self)


class ObjectApiResponse(Generic[_ObjectBodyType], ApiResponse[Dict[str, Any]]):
    """API responses which are for a JSON object"""

    def __getitem__(self, item: str) -> Any:
        return self.body[item]  # type: ignore[index]

    def __iter__(self) -> Iterator[str]:
        return iter(self._body)

    @property
    def body(self) -> _ObjectBodyType:  # type: ignore[override]
        return self._body  # type: ignore[no-any-return]


class ListApiResponse(
    Generic[_ListItemBodyType],
    ApiResponse[List[Any]],
):
    """API responses which are a list of items. Can be NDJSON or a JSON list"""

    @overload
    def __getitem__(self, item: slice) -> List[_ListItemBodyType]: ...

    @overload
    def __getitem__(self, item: int) -> _ListItemBodyType: ...

    def __getitem__(
        self, item: Union[int, slice]
    ) -> Union[_ListItemBodyType, List[_ListItemBodyType]]:
        return self.body[item]

    def __iter__(self) -> Iterator[_ListItemBodyType]:
        return iter(self.body)

    @property
    def body(self) -> List[_ListItemBodyType]:
        return self._body  # type: ignore[no-any-return]
