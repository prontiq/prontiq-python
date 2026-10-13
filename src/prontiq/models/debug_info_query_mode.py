from typing import Literal

DebugInfoQueryMode = Literal["autocomplete", "enrich", "lookup", "reverse", "validate"]

DEBUG_INFO_QUERY_MODE_VALUES: set[DebugInfoQueryMode] = {
    "autocomplete",
    "enrich",
    "lookup",
    "reverse",
    "validate",
}


def check_debug_info_query_mode(value: str) -> DebugInfoQueryMode:
    if value in DEBUG_INFO_QUERY_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DEBUG_INFO_QUERY_MODE_VALUES!r}"
    )
