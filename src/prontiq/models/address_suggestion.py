from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.australian_state_code import (
    AustralianStateCode,
    check_australian_state_code,
)
from ..models.prontiq_match_quality import (
    ProntiqMatchQuality,
    check_prontiq_match_quality,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debug_info import DebugInfo


T = TypeVar("T", bound="AddressSuggestion")


@_attrs_define
class AddressSuggestion:
    """Autocomplete suggestion containing display fields and Prontiq-computed match quality. G-NAF confidence and internal
    search relevance are not returned in default suggestions.

        Example:
            {'id': 'GAQLD156786950', 'addressLabel': '9 ENDEAVOUR COURT', 'localityName': 'LAMMERMOOR', 'state': 'QLD',
                'postcode': '4703', 'prontiqMatchScore': 92, 'prontiqMatchQuality': 'high'}

        Attributes:
            id (str): Opaque G-NAF persistent identifier for this suggestion. Store it when a user selects the suggestion,
                then pass it to Enrich for the full address document. Example: GAQLD156786950.
            prontiq_match_score (int): Prontiq-computed request match score from 0 to 100. Use it to decide whether to
                accept, confirm, or reject a returned address for the submitted request. It is not G-NAF source confidence,
                deliverability, or geocode precision. Example: 92.
            prontiq_match_quality (ProntiqMatchQuality): Human-readable Prontiq match-quality bucket derived from
                `prontiqMatchScore`: `high` is 67-100, `medium` is 34-66, `low` is 1-33, and `none` is 0. Example: high.
            address_label (None | str | Unset):
            locality_name (None | str | Unset):
            state (AustralianStateCode | None | Unset):
            postcode (None | str | Unset):
            debug (DebugInfo | Unset): Optional diagnostic metadata returned only when `debug=true` is supplied. Debug
                values are for support and troubleshooting, not production decision-making. Example: {'scoringVersion':
                'address-match-v1', 'queryMode': 'autocomplete', 'searchScore': 42.1}.
    """

    id: str
    prontiq_match_score: int
    prontiq_match_quality: ProntiqMatchQuality
    address_label: None | str | Unset = UNSET
    locality_name: None | str | Unset = UNSET
    state: AustralianStateCode | None | Unset = UNSET
    postcode: None | str | Unset = UNSET
    debug: DebugInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        prontiq_match_score = self.prontiq_match_score

        prontiq_match_quality: str = self.prontiq_match_quality

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

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "prontiqMatchScore": prontiq_match_score,
                "prontiqMatchQuality": prontiq_match_quality,
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
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debug_info import DebugInfo  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        prontiq_match_score = d.pop("prontiqMatchScore")

        prontiq_match_quality = check_prontiq_match_quality(
            d.pop("prontiqMatchQuality")
        )

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

        _debug = d.pop("debug", UNSET)
        debug: DebugInfo | Unset
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = DebugInfo.from_dict(_debug)

        address_suggestion = cls(
            id=id,
            prontiq_match_score=prontiq_match_score,
            prontiq_match_quality=prontiq_match_quality,
            address_label=address_label,
            locality_name=locality_name,
            state=state,
            postcode=postcode,
            debug=debug,
        )

        address_suggestion.additional_properties = d
        return address_suggestion

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
