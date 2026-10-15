from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Geocode")


@_attrs_define
class Geocode:
    """G-NAF geocoding metadata and decimal-degree coordinates for the address.

    Example:
        {'latitude': -23.1601, 'longitude': 150.7596, 'type': 'PROPERTY CENTROID', 'reliability': 2}

    Attributes:
        latitude (float): GDA2020 (EPSG:7844) decimal-degree coordinate used for Australian address locations and
            reverse-geocode queries. Example: -23.1601.
        longitude (float): GDA2020 (EPSG:7844) decimal-degree coordinate used for Australian address locations and
            reverse-geocode queries. Example: -23.1601.
        type_ (None | str | Unset):
        reliability (int | None | Unset):
    """

    latitude: float
    longitude: float
    type_: None | str | Unset = UNSET
    reliability: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        reliability: int | None | Unset
        if isinstance(self.reliability, Unset):
            reliability = UNSET
        else:
            reliability = self.reliability

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latitude": latitude,
                "longitude": longitude,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if reliability is not UNSET:
            field_dict["reliability"] = reliability

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_reliability(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reliability = _parse_reliability(d.pop("reliability", UNSET))

        geocode = cls(
            latitude=latitude,
            longitude=longitude,
            type_=type_,
            reliability=reliability,
        )

        geocode.additional_properties = d
        return geocode

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
