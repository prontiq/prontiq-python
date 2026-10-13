from typing import Literal

AustralianStateCode = Literal["ACT", "NSW", "NT", "OT", "QLD", "SA", "TAS", "VIC", "WA"]

AUSTRALIAN_STATE_CODE_VALUES: set[AustralianStateCode] = {
    "ACT",
    "NSW",
    "NT",
    "OT",
    "QLD",
    "SA",
    "TAS",
    "VIC",
    "WA",
}


def check_australian_state_code(value: str) -> AustralianStateCode:
    if value in AUSTRALIAN_STATE_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AUSTRALIAN_STATE_CODE_VALUES!r}"
    )
