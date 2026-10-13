from typing import Literal

ProntiqMatchQuality = Literal["high", "low", "medium", "none"]

PRONTIQ_MATCH_QUALITY_VALUES: set[ProntiqMatchQuality] = {
    "high",
    "low",
    "medium",
    "none",
}


def check_prontiq_match_quality(value: str) -> ProntiqMatchQuality:
    if value in PRONTIQ_MATCH_QUALITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRONTIQ_MATCH_QUALITY_VALUES!r}"
    )
