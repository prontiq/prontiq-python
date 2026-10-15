from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_suggestion import AddressSuggestion
    from ..models.debug_info import DebugInfo


T = TypeVar("T", bound="AutocompleteAddressResponse")


@_attrs_define
class AutocompleteAddressResponse:
    """Autocomplete suggestions for a partial address query. Suggestions include Prontiq-computed match quality; G-NAF
    confidence and internal search relevance are not returned in default responses.

        Example:
            {'suggestions': [{'id': 'GAQLD156786950', 'addressLabel': '9 ENDEAVOUR COURT', 'localityName': 'LAMMERMOOR',
                'state': 'QLD', 'postcode': '4703', 'prontiqMatchScore': 92, 'prontiqMatchQuality': 'high'}], 'total': 1}

        Attributes:
            suggestions (list[AddressSuggestion]): Suggested address records ordered for autocomplete display. The array may
                be empty when no candidate addresses match the query.
            total (int): Number of suggestions returned in this response. Example: 1.
            debug (DebugInfo | Unset): Optional diagnostic metadata returned only when `debug=true` is supplied. Debug
                values are for support and troubleshooting, not production decision-making. Example: {'scoringVersion':
                'address-match-v1', 'queryMode': 'autocomplete', 'searchScore': 42.1}.
    """

    suggestions: list[AddressSuggestion]
    total: int
    debug: DebugInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggestions = []
        for suggestions_item_data in self.suggestions:
            suggestions_item = suggestions_item_data.to_dict()
            suggestions.append(suggestions_item)

        total = self.total

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suggestions": suggestions,
                "total": total,
            }
        )
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_suggestion import AddressSuggestion  # noqa: PLC0415
        from ..models.debug_info import DebugInfo  # noqa: PLC0415

        d = dict(src_dict)
        suggestions = []
        _suggestions = d.pop("suggestions")
        for suggestions_item_data in _suggestions:
            suggestions_item = AddressSuggestion.from_dict(suggestions_item_data)

            suggestions.append(suggestions_item)

        total = d.pop("total")

        _debug = d.pop("debug", UNSET)
        debug: DebugInfo | Unset
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = DebugInfo.from_dict(_debug)

        autocomplete_address_response = cls(
            suggestions=suggestions,
            total=total,
            debug=debug,
        )

        autocomplete_address_response.additional_properties = d
        return autocomplete_address_response

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
