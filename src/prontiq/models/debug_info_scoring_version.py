from typing import Literal

DebugInfoScoringVersion = Literal["address-match-v1"]

DEBUG_INFO_SCORING_VERSION_VALUES: set[DebugInfoScoringVersion] = {
    "address-match-v1",
}


def check_debug_info_scoring_version(value: str) -> DebugInfoScoringVersion:
    if value in DEBUG_INFO_SCORING_VERSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DEBUG_INFO_SCORING_VERSION_VALUES!r}"
    )
