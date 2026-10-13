from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.address_error_code import AddressErrorCode, check_address_error_code
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_error_response_error_details import (
        AddressErrorResponseErrorDetails,
    )


T = TypeVar("T", bound="AddressErrorResponseError")


@_attrs_define
class AddressErrorResponseError:
    """Nested error object containing the machine code, human message, HTTP status, and request id.

    Example:
        {'code': 'INVALID_PARAMETERS', 'message': 'Invalid query parameters', 'status': 400, 'request_id':
            'req_01HZX7A8J5K9P4R2QW3E6T7Y8Z'}

    Attributes:
        code (AddressErrorCode): Stable machine-readable public Address API error code. Use this value for branching
            instead of parsing the human-readable `message`. Example: INVALID_PARAMETERS.
        message (str): Human-readable error message. Example: Invalid query parameters.
        status (int): HTTP status code. Example: 400.
        request_id (str): Request identifier for support and debugging. This snake_case field is stable in v1. Example:
            req_01HZX7A8J5K9P4R2QW3E6T7Y8Z.
        details (AddressErrorResponseErrorDetails | Unset): Optional structured details. Shape depends on the error
            code. Example: {'q': ['Required']}.
    """

    code: AddressErrorCode
    message: str
    status: int
    request_id: str
    details: AddressErrorResponseErrorDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: str = self.code

        message = self.message

        status = self.status

        request_id = self.request_id

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "status": status,
                "request_id": request_id,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_error_response_error_details import (
            AddressErrorResponseErrorDetails,  # noqa: PLC0415
        )

        d = dict(src_dict)
        code = check_address_error_code(d.pop("code"))

        message = d.pop("message")

        status = d.pop("status")

        request_id = d.pop("request_id")

        _details = d.pop("details", UNSET)
        details: AddressErrorResponseErrorDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = AddressErrorResponseErrorDetails.from_dict(_details)

        address_error_response_error = cls(
            code=code,
            message=message,
            status=status,
            request_id=request_id,
            details=details,
        )

        address_error_response_error.additional_properties = d
        return address_error_response_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
