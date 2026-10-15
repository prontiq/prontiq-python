from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecondaryAddress")


@_attrs_define
class SecondaryAddress:
    """Secondary or child address associated with an enriched primary address.

    Example:
        {'id': 'GAVIC425495838', 'addressLabel': 'SHOP 1 1 MCNAB AVENUE'}

    Attributes:
        id (None | str | Unset):
        address_label (None | str | Unset):
    """

    id: None | str | Unset = UNSET
    address_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        address_label: None | str | Unset
        if isinstance(self.address_label, Unset):
            address_label = UNSET
        else:
            address_label = self.address_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if address_label is not UNSET:
            field_dict["addressLabel"] = address_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_address_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_label = _parse_address_label(d.pop("addressLabel", UNSET))

        secondary_address = cls(
            id=id,
            address_label=address_label,
        )

        secondary_address.additional_properties = d
        return secondary_address

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
