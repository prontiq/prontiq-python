from typing import Literal

FallbackGeocodeType0Precision = Literal["locality", "street", "unknown"]

FALLBACK_GEOCODE_TYPE_0_PRECISION_VALUES: set[FallbackGeocodeType0Precision] = {
    "locality",
    "street",
    "unknown",
}


def check_fallback_geocode_type_0_precision(
    value: str,
) -> FallbackGeocodeType0Precision:
    if value in FALLBACK_GEOCODE_TYPE_0_PRECISION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FALLBACK_GEOCODE_TYPE_0_PRECISION_VALUES!r}"
    )
