from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.australian_state_code import (
    AustralianStateCode,
    check_australian_state_code,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_boundaries import AddressBoundaries
    from ..models.fallback_geocode_type_0 import FallbackGeocodeType0
    from ..models.geocode import Geocode
    from ..models.location import Location


T = TypeVar("T", bound="AddressDocument")


@_attrs_define
class AddressDocument:
    """Standard public address record returned by Validate and Reverse geocode, and used as the base for Enrich. Optional
    fields may be absent or null when the source data does not provide that attribute.

        Example:
            {'id': 'GAQLD156786950', 'addressLabel': '9 ENDEAVOUR COURT', 'localityName': 'LAMMERMOOR', 'state': 'QLD',
                'postcode': '4703', 'confidence': 2, 'fallbackGeocode': None}

        Attributes:
            id (str): Opaque G-NAF persistent identifier for this address record. Store it as a string and pass it to Enrich
                when you need the full public address document. Example: GAQLD156786950.
            fallback_geocode (FallbackGeocodeType0 | None): Default coordinates only when a primary site point is
                unavailable; otherwise null.
            address_label (None | str | Unset):
            locality_name (None | str | Unset):
            state (AustralianStateCode | None | Unset):
            postcode (None | str | Unset):
            confidence (int | None | Unset):
            geocode (Geocode | None | Unset):
            location (Location | None | Unset):
            boundaries (AddressBoundaries | None | Unset):
    """

    id: str
    fallback_geocode: FallbackGeocodeType0 | None
    address_label: None | str | Unset = UNSET
    locality_name: None | str | Unset = UNSET
    state: AustralianStateCode | None | Unset = UNSET
    postcode: None | str | Unset = UNSET
    confidence: int | None | Unset = UNSET
    geocode: Geocode | None | Unset = UNSET
    location: Location | None | Unset = UNSET
    boundaries: AddressBoundaries | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.address_boundaries import AddressBoundaries  # noqa: PLC0415
        from ..models.fallback_geocode_type_0 import (
            FallbackGeocodeType0,  # noqa: PLC0415
        )
        from ..models.geocode import Geocode  # noqa: PLC0415
        from ..models.location import Location  # noqa: PLC0415

        id = self.id

        fallback_geocode: dict[str, Any] | None
        if isinstance(self.fallback_geocode, FallbackGeocodeType0):
            fallback_geocode = self.fallback_geocode.to_dict()
        else:
            fallback_geocode = self.fallback_geocode

        address_label: None | str | Unset
        if isinstance(self.address_label, Unset):
            address_label = UNSET
        else:
            address_label = self.address_label

        locality_name: None | str | Unset
        if isinstance(self.locality_name, Unset):
            locality_name = UNSET
        else:
            locality_name = self.locality_name

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, str):
            state = self.state
        else:
            state = self.state

        postcode: None | str | Unset
        if isinstance(self.postcode, Unset):
            postcode = UNSET
        else:
            postcode = self.postcode

        confidence: int | None | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        geocode: dict[str, Any] | None | Unset
        if isinstance(self.geocode, Unset):
            geocode = UNSET
        elif isinstance(self.geocode, Geocode):
            geocode = self.geocode.to_dict()
        else:
            geocode = self.geocode

        location: dict[str, Any] | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, Location):
            location = self.location.to_dict()
        else:
            location = self.location

        boundaries: dict[str, Any] | None | Unset
        if isinstance(self.boundaries, Unset):
            boundaries = UNSET
        elif isinstance(self.boundaries, AddressBoundaries):
            boundaries = self.boundaries.to_dict()
        else:
            boundaries = self.boundaries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fallbackGeocode": fallback_geocode,
            }
        )
        if address_label is not UNSET:
            field_dict["addressLabel"] = address_label
        if locality_name is not UNSET:
            field_dict["localityName"] = locality_name
        if state is not UNSET:
            field_dict["state"] = state
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if geocode is not UNSET:
            field_dict["geocode"] = geocode
        if location is not UNSET:
            field_dict["location"] = location
        if boundaries is not UNSET:
            field_dict["boundaries"] = boundaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_boundaries import AddressBoundaries  # noqa: PLC0415
        from ..models.fallback_geocode_type_0 import (
            FallbackGeocodeType0,  # noqa: PLC0415
        )
        from ..models.geocode import Geocode  # noqa: PLC0415
        from ..models.location import Location  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_fallback_geocode(data: object) -> FallbackGeocodeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_fallback_geocode_type_0 = (
                    FallbackGeocodeType0.from_dict(data)
                )

                return componentsschemas_fallback_geocode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FallbackGeocodeType0 | None, data)

        fallback_geocode = _parse_fallback_geocode(d.pop("fallbackGeocode"))

        def _parse_address_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_label = _parse_address_label(d.pop("addressLabel", UNSET))

        def _parse_locality_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locality_name = _parse_locality_name(d.pop("localityName", UNSET))

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

        def _parse_postcode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postcode = _parse_postcode(d.pop("postcode", UNSET))

        def _parse_confidence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_geocode(data: object) -> Geocode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geocode_type_0 = Geocode.from_dict(data)

                return geocode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Geocode | None | Unset, data)

        geocode = _parse_geocode(d.pop("geocode", UNSET))

        def _parse_location(data: object) -> Location | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_0 = Location.from_dict(data)

                return location_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Location | None | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_boundaries(data: object) -> AddressBoundaries | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                boundaries_type_0 = AddressBoundaries.from_dict(data)

                return boundaries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddressBoundaries | None | Unset, data)

        boundaries = _parse_boundaries(d.pop("boundaries", UNSET))

        address_document = cls(
            id=id,
            fallback_geocode=fallback_geocode,
            address_label=address_label,
            locality_name=locality_name,
            state=state,
            postcode=postcode,
            confidence=confidence,
            geocode=geocode,
            location=location,
            boundaries=boundaries,
        )

        address_document.additional_properties = d
        return address_document

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
