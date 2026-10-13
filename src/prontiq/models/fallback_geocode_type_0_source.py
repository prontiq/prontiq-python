from typing import Literal

FallbackGeocodeType0Source = Literal["GNAF_DEFAULT"]

FALLBACK_GEOCODE_TYPE_0_SOURCE_VALUES: set[FallbackGeocodeType0Source] = {
    "GNAF_DEFAULT",
}


def check_fallback_geocode_type_0_source(value: str) -> FallbackGeocodeType0Source:
    if value in FALLBACK_GEOCODE_TYPE_0_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FALLBACK_GEOCODE_TYPE_0_SOURCE_VALUES!r}"
    )
