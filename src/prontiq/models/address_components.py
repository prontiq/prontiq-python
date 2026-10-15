from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressComponents")


@_attrs_define
class AddressComponents:
    """Structured address components when available for the enriched record.

    Example:
        {'flatType': 'FLAT', 'flatNumber': '14', 'streetNumberFirst': '5', 'streetName': 'DUKE', 'streetType': 'STREET'}

    Attributes:
        address_site_name (None | str | Unset):
        building_name (None | str | Unset):
        flat_type (None | str | Unset):
        flat_number (None | str | Unset):
        level_type (None | str | Unset):
        level_number (None | str | Unset):
        lot_number (None | str | Unset):
        street_number_first (None | str | Unset):
        street_number_last (None | str | Unset):
        street_name (None | str | Unset):
        street_type (None | str | Unset):
        street_suffix (None | str | Unset):
    """

    address_site_name: None | str | Unset = UNSET
    building_name: None | str | Unset = UNSET
    flat_type: None | str | Unset = UNSET
    flat_number: None | str | Unset = UNSET
    level_type: None | str | Unset = UNSET
    level_number: None | str | Unset = UNSET
    lot_number: None | str | Unset = UNSET
    street_number_first: None | str | Unset = UNSET
    street_number_last: None | str | Unset = UNSET
    street_name: None | str | Unset = UNSET
    street_type: None | str | Unset = UNSET
    street_suffix: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_site_name: None | str | Unset
        if isinstance(self.address_site_name, Unset):
            address_site_name = UNSET
        else:
            address_site_name = self.address_site_name

        building_name: None | str | Unset
        if isinstance(self.building_name, Unset):
            building_name = UNSET
        else:
            building_name = self.building_name

        flat_type: None | str | Unset
        if isinstance(self.flat_type, Unset):
            flat_type = UNSET
        else:
            flat_type = self.flat_type

        flat_number: None | str | Unset
        if isinstance(self.flat_number, Unset):
            flat_number = UNSET
        else:
            flat_number = self.flat_number

        level_type: None | str | Unset
        if isinstance(self.level_type, Unset):
            level_type = UNSET
        else:
            level_type = self.level_type

        level_number: None | str | Unset
        if isinstance(self.level_number, Unset):
            level_number = UNSET
        else:
            level_number = self.level_number

        lot_number: None | str | Unset
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        street_number_first: None | str | Unset
        if isinstance(self.street_number_first, Unset):
            street_number_first = UNSET
        else:
            street_number_first = self.street_number_first

        street_number_last: None | str | Unset
        if isinstance(self.street_number_last, Unset):
            street_number_last = UNSET
        else:
            street_number_last = self.street_number_last

        street_name: None | str | Unset
        if isinstance(self.street_name, Unset):
            street_name = UNSET
        else:
            street_name = self.street_name

        street_type: None | str | Unset
        if isinstance(self.street_type, Unset):
            street_type = UNSET
        else:
            street_type = self.street_type

        street_suffix: None | str | Unset
        if isinstance(self.street_suffix, Unset):
            street_suffix = UNSET
        else:
            street_suffix = self.street_suffix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_site_name is not UNSET:
            field_dict["addressSiteName"] = address_site_name
        if building_name is not UNSET:
            field_dict["buildingName"] = building_name
        if flat_type is not UNSET:
            field_dict["flatType"] = flat_type
        if flat_number is not UNSET:
            field_dict["flatNumber"] = flat_number
        if level_type is not UNSET:
            field_dict["levelType"] = level_type
        if level_number is not UNSET:
            field_dict["levelNumber"] = level_number
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if street_number_first is not UNSET:
            field_dict["streetNumberFirst"] = street_number_first
        if street_number_last is not UNSET:
            field_dict["streetNumberLast"] = street_number_last
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if street_type is not UNSET:
            field_dict["streetType"] = street_type
        if street_suffix is not UNSET:
            field_dict["streetSuffix"] = street_suffix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_address_site_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_site_name = _parse_address_site_name(d.pop("addressSiteName", UNSET))

        def _parse_building_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_name = _parse_building_name(d.pop("buildingName", UNSET))

        def _parse_flat_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat_type = _parse_flat_type(d.pop("flatType", UNSET))

        def _parse_flat_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flat_number = _parse_flat_number(d.pop("flatNumber", UNSET))

        def _parse_level_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level_type = _parse_level_type(d.pop("levelType", UNSET))

        def _parse_level_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level_number = _parse_level_number(d.pop("levelNumber", UNSET))

        def _parse_lot_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))

        def _parse_street_number_first(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_number_first = _parse_street_number_first(
            d.pop("streetNumberFirst", UNSET)
        )

        def _parse_street_number_last(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_number_last = _parse_street_number_last(d.pop("streetNumberLast", UNSET))

        def _parse_street_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_name = _parse_street_name(d.pop("streetName", UNSET))

        def _parse_street_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_type = _parse_street_type(d.pop("streetType", UNSET))

        def _parse_street_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_suffix = _parse_street_suffix(d.pop("streetSuffix", UNSET))

        address_components = cls(
            address_site_name=address_site_name,
            building_name=building_name,
            flat_type=flat_type,
            flat_number=flat_number,
            level_type=level_type,
            level_number=level_number,
            lot_number=lot_number,
            street_number_first=street_number_first,
            street_number_last=street_number_last,
            street_name=street_name,
            street_type=street_type,
            street_suffix=street_suffix,
        )

        address_components.additional_properties = d
        return address_components

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
