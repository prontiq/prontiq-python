from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.australian_state_code import (
    AustralianStateCode,
    check_australian_state_code,
)
from ..models.enriched_address_document_address_role_type_0 import (
    EnrichedAddressDocumentAddressRoleType0,
    check_enriched_address_document_address_role_type_0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_alias import AddressAlias
    from ..models.address_boundaries import AddressBoundaries
    from ..models.address_components import AddressComponents
    from ..models.all_geocode import AllGeocode
    from ..models.debug_info import DebugInfo
    from ..models.fallback_geocode_type_0 import FallbackGeocodeType0
    from ..models.geocode import Geocode
    from ..models.locality_context import LocalityContext
    from ..models.location import Location
    from ..models.secondary_address import SecondaryAddress
    from ..models.street_context import StreetContext


T = TypeVar("T", bound="EnrichAddressResponse")


@_attrs_define
class EnrichAddressResponse:
    """Enrich-only address document with structured components, extra geocodes, locality and street context, aliases,
    secondaries, extended boundaries, and optional diagnostic metadata when debug=true.

        Example:
            {'id': 'GAVIC411087566', 'addressLabel': 'FLAT 14, 5 DUKE STREET', 'localityName': 'CAULFIELD SOUTH', 'state':
                'VIC', 'postcode': '3162', 'confidence': 2, 'fallbackGeocode': None, 'sourceDataRelease': '2026.08',
                'addressRole': 'SECONDARY', 'legalParcelId': '14\\\\PS349838', 'components': {'flatType': 'FLAT', 'flatNumber':
                '14', 'streetNumberFirst': '5', 'streetName': 'DUKE', 'streetType': 'STREET'}, 'boundaries': {'lga': {'name':
                'Glen Eira', 'code': 'lga9bd137c30d17'}, 'ward': {'name': 'Bambra Ward'}, 'sa1': '20802117831'}}

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
            source_data_release (None | str | Unset):
            address_role (EnrichedAddressDocumentAddressRoleType0 | None | Unset):
            components (AddressComponents | Unset): Structured address components when available for the enriched record.
                Example: {'flatType': 'FLAT', 'flatNumber': '14', 'streetNumberFirst': '5', 'streetName': 'DUKE', 'streetType':
                'STREET'}.
            legal_parcel_id (None | str | Unset):
            all_geocodes (list[AllGeocode] | Unset): Additional geocodes associated with the address. The array preserves
                source order after invalid coordinates are removed. Example: [{'latitude': -37.89180933, 'longitude':
                145.01510717, 'type': 'FRONTAGE CENTRE SETBACK', 'reliability': 2}, {'latitude': -37.89180905, 'longitude':
                145.01490263, 'type': 'PROPERTY CENTROID', 'reliability': 2}].
            locality (LocalityContext | Unset): Locality context when available for the enriched address. Example: {'id':
                'loc1b5a0e70afd4', 'classification': 'GAZETTED LOCALITY', 'neighbours': ['ELSTERNWICK', 'GARDENVALE', 'ORMOND'],
                'aliases': []}.
            street (StreetContext | Unset): Street context when available for the enriched address. Example: {'id':
                'VIC1953679', 'classification': 'CONFIRMED', 'aliases': []}.
            aliases (list[AddressAlias] | Unset): Alternative address labels associated with the enriched address.
            secondaries (list[SecondaryAddress] | Unset): Secondary or child addresses associated with the enriched address.
            debug (DebugInfo | Unset): Optional diagnostic metadata returned only when `debug=true` is supplied. Debug
                values are for support and troubleshooting, not production decision-making. Example: {'scoringVersion':
                'address-match-v1', 'queryMode': 'autocomplete', 'searchScore': 42.1}.
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
    source_data_release: None | str | Unset = UNSET
    address_role: EnrichedAddressDocumentAddressRoleType0 | None | Unset = UNSET
    components: AddressComponents | Unset = UNSET
    legal_parcel_id: None | str | Unset = UNSET
    all_geocodes: list[AllGeocode] | Unset = UNSET
    locality: LocalityContext | Unset = UNSET
    street: StreetContext | Unset = UNSET
    aliases: list[AddressAlias] | Unset = UNSET
    secondaries: list[SecondaryAddress] | Unset = UNSET
    debug: DebugInfo | Unset = UNSET
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

        source_data_release: None | str | Unset
        if isinstance(self.source_data_release, Unset):
            source_data_release = UNSET
        else:
            source_data_release = self.source_data_release

        address_role: None | str | Unset
        if isinstance(self.address_role, Unset):
            address_role = UNSET
        elif isinstance(self.address_role, str):
            address_role = self.address_role
        else:
            address_role = self.address_role

        components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.components, Unset):
            components = self.components.to_dict()

        legal_parcel_id: None | str | Unset
        if isinstance(self.legal_parcel_id, Unset):
            legal_parcel_id = UNSET
        else:
            legal_parcel_id = self.legal_parcel_id

        all_geocodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_geocodes, Unset):
            all_geocodes = []
            for all_geocodes_item_data in self.all_geocodes:
                all_geocodes_item = all_geocodes_item_data.to_dict()
                all_geocodes.append(all_geocodes_item)

        locality: dict[str, Any] | Unset = UNSET
        if not isinstance(self.locality, Unset):
            locality = self.locality.to_dict()

        street: dict[str, Any] | Unset = UNSET
        if not isinstance(self.street, Unset):
            street = self.street.to_dict()

        aliases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()
                aliases.append(aliases_item)

        secondaries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secondaries, Unset):
            secondaries = []
            for secondaries_item_data in self.secondaries:
                secondaries_item = secondaries_item_data.to_dict()
                secondaries.append(secondaries_item)

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

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
        if source_data_release is not UNSET:
            field_dict["sourceDataRelease"] = source_data_release
        if address_role is not UNSET:
            field_dict["addressRole"] = address_role
        if components is not UNSET:
            field_dict["components"] = components
        if legal_parcel_id is not UNSET:
            field_dict["legalParcelId"] = legal_parcel_id
        if all_geocodes is not UNSET:
            field_dict["allGeocodes"] = all_geocodes
        if locality is not UNSET:
            field_dict["locality"] = locality
        if street is not UNSET:
            field_dict["street"] = street
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if secondaries is not UNSET:
            field_dict["secondaries"] = secondaries
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_alias import AddressAlias  # noqa: PLC0415
        from ..models.address_boundaries import AddressBoundaries  # noqa: PLC0415
        from ..models.address_components import AddressComponents  # noqa: PLC0415
        from ..models.all_geocode import AllGeocode  # noqa: PLC0415
        from ..models.debug_info import DebugInfo  # noqa: PLC0415
        from ..models.fallback_geocode_type_0 import (
            FallbackGeocodeType0,  # noqa: PLC0415
        )
        from ..models.geocode import Geocode  # noqa: PLC0415
        from ..models.locality_context import LocalityContext  # noqa: PLC0415
        from ..models.location import Location  # noqa: PLC0415
        from ..models.secondary_address import SecondaryAddress  # noqa: PLC0415
        from ..models.street_context import StreetContext  # noqa: PLC0415

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

        def _parse_source_data_release(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_data_release = _parse_source_data_release(
            d.pop("sourceDataRelease", UNSET)
        )

        def _parse_address_role(
            data: object,
        ) -> EnrichedAddressDocumentAddressRoleType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                address_role_type_0 = (
                    check_enriched_address_document_address_role_type_0(data)
                )

                return address_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnrichedAddressDocumentAddressRoleType0 | None | Unset, data)

        address_role = _parse_address_role(d.pop("addressRole", UNSET))

        _components = d.pop("components", UNSET)
        components: AddressComponents | Unset
        if isinstance(_components, Unset):
            components = UNSET
        else:
            components = AddressComponents.from_dict(_components)

        def _parse_legal_parcel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_parcel_id = _parse_legal_parcel_id(d.pop("legalParcelId", UNSET))

        _all_geocodes = d.pop("allGeocodes", UNSET)
        all_geocodes: list[AllGeocode] | Unset = UNSET
        if _all_geocodes is not UNSET:
            all_geocodes = []
            for all_geocodes_item_data in _all_geocodes:
                all_geocodes_item = AllGeocode.from_dict(all_geocodes_item_data)

                all_geocodes.append(all_geocodes_item)

        _locality = d.pop("locality", UNSET)
        locality: LocalityContext | Unset
        if isinstance(_locality, Unset):
            locality = UNSET
        else:
            locality = LocalityContext.from_dict(_locality)

        _street = d.pop("street", UNSET)
        street: StreetContext | Unset
        if isinstance(_street, Unset):
            street = UNSET
        else:
            street = StreetContext.from_dict(_street)

        _aliases = d.pop("aliases", UNSET)
        aliases: list[AddressAlias] | Unset = UNSET
        if _aliases is not UNSET:
            aliases = []
            for aliases_item_data in _aliases:
                aliases_item = AddressAlias.from_dict(aliases_item_data)

                aliases.append(aliases_item)

        _secondaries = d.pop("secondaries", UNSET)
        secondaries: list[SecondaryAddress] | Unset = UNSET
        if _secondaries is not UNSET:
            secondaries = []
            for secondaries_item_data in _secondaries:
                secondaries_item = SecondaryAddress.from_dict(secondaries_item_data)

                secondaries.append(secondaries_item)

        _debug = d.pop("debug", UNSET)
        debug: DebugInfo | Unset
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = DebugInfo.from_dict(_debug)

        enrich_address_response = cls(
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
            source_data_release=source_data_release,
            address_role=address_role,
            components=components,
            legal_parcel_id=legal_parcel_id,
            all_geocodes=all_geocodes,
            locality=locality,
            street=street,
            aliases=aliases,
            secondaries=secondaries,
            debug=debug,
        )

        enrich_address_response.additional_properties = d
        return enrich_address_response

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
