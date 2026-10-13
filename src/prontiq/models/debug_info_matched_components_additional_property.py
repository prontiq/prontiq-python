from typing import Literal

DebugInfoMatchedComponentsAdditionalProperty = Literal[
    "exact", "fuzzy", "none", "prefix"
]

DEBUG_INFO_MATCHED_COMPONENTS_ADDITIONAL_PROPERTY_VALUES: set[
    DebugInfoMatchedComponentsAdditionalProperty
] = {
    "exact",
    "fuzzy",
    "none",
    "prefix",
}


def check_debug_info_matched_components_additional_property(
    value: str,
) -> DebugInfoMatchedComponentsAdditionalProperty:
    if value in DEBUG_INFO_MATCHED_COMPONENTS_ADDITIONAL_PROPERTY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DEBUG_INFO_MATCHED_COMPONENTS_ADDITIONAL_PROPERTY_VALUES!r}"
    )
