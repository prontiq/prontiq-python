from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.australian_state_code import (
    AustralianStateCode,
    check_australian_state_code,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostcodeLocalitySummary")


@_attrs_define
class PostcodeLocalitySummary:
    """Locality summary returned for a postcode lookup.

    Example:
        {'name': 'SYDNEY', 'state': 'NSW', 'address_count': 12345}

    Attributes:
        name (str): Official suburb or locality name associated with the postcode. Example: SYDNEY.
        address_count (int): Number of address records in this locality for the requested postcode. This is dataset
            cardinality, not credit usage. Example: 12345.
        state (AustralianStateCode | None | Unset): Australian state or territory for the locality when available. The
            value is uppercase in responses. Example: NSW.
    """

    name: str
    address_count: int
    state: AustralianStateCode | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address_count = self.address_count

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, str):
            state = self.state
        else:
            state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "address_count": address_count,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        address_count = d.pop("address_count")

        def _parse_state(data: object) -> AustralianStateCode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = check_australian_state_code(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AustralianStateCode | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        postcode_locality_summary = cls(
            name=name,
            address_count=address_count,
            state=state,
        )

        postcode_locality_summary.additional_properties = d
        return postcode_locality_summary

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
