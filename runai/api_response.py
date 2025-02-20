"""API response object."""

from __future__ import annotations
from typing import Optional, Generic, Mapping, TypeVar
from pydantic import Field, StrictInt, BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """
    API response object
    """

    status_code: StrictInt = Field(description="HTTP status code")
    headers: Optional[Mapping[str, str]] = Field(None, description="HTTP headers")
    data: T = Field(description="Deserialized data given the data type")

    model_config = {"arbitrary_types_allowed": True}
