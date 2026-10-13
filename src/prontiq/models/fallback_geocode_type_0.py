from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fallback_geocode_type_0_precision import (
    FallbackGeocodeType0Precision,
    check_fallback_geocode_type_0_precision,
)
from ..models.fallback_geocode_type_0_source import (
    FallbackGeocodeType0Source,
    check_fallback_geocode_type_0_source,
)

T = TypeVar("T", bound="FallbackGeocodeType0")


@_attrs_define
class FallbackGeocodeType0:
    """Default coordinates only when a primary site point is unavailable; otherwise null.

    Attributes:
        latitude (float): Default latitude in native GDA2020 (EPSG:7844) decimal degrees. Example: -12.20477449.
        longitude (float): Default longitude in native GDA2020 (EPSG:7844) decimal degrees. Example: 96.84370912.
        type_code (str): G-NAF default geocode type code: STL for street, LOC for locality, or another source code.
            Example: STL.
        type_ (str): G-NAF default geocode type label. Example: STREET LOCALITY.
        source (FallbackGeocodeType0Source): Identifies the default geocode source. Example: GNAF_DEFAULT.
        precision (FallbackGeocodeType0Precision): Coarse spatial precision. Unknown means the source type is neither
            STL nor LOC. Example: street.
    """

    latitude: float
    longitude: float
    type_code: str
    type_: str
    source: FallbackGeocodeType0Source
    precision: FallbackGeocodeType0Precision
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        type_code = self.type_code

        type_ = self.type_

        source: str = self.source

        precision: str = self.precision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latitude": latitude,
                "longitude": longitude,
                "typeCode": type_code,
                "type": type_,
                "source": source,
                "precision": precision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        type_code = d.pop("typeCode")

        type_ = d.pop("type")

        source = check_fallback_geocode_type_0_source(d.pop("source"))

        precision = check_fallback_geocode_type_0_precision(d.pop("precision"))

        fallback_geocode_type_0 = cls(
            latitude=latitude,
            longitude=longitude,
            type_code=type_code,
            type_=type_,
            source=source,
            precision=precision,
        )

        fallback_geocode_type_0.additional_properties = d
        return fallback_geocode_type_0

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
