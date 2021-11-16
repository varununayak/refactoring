# Parametrize Function

import math


def bottom_band(usage: float):
    return min(usage, 100)


def mid_band(usage: float):
    return min(usage, 200) - 100 if usage > 100 else 0


def top_band(usage: float):
    return usage - 200 if usage > 200 else 0


def base_charge(usage: float) -> float:
    if usage < 0:
        return 0
    return bottom_band(usage) * 0.03 + \
        mid_band(usage) * 0.05 + \
        top_band(usage) * 0.07


"""
If two functions carry out similar logic with different literal values,
we can remove the duplication by using a single function with parameters
for different values. This increases the usefulness of function for the future.
"""


def within_band_usage(usage: float, bottom: float, top: float):
    return usage if bottom <= usage < top else 0


def base_charge_refactored(usage: float) -> float:
    # This guard clause technically not required anymore, but we'll keep it for clarity
    if usage < 0:
        return 0
    return within_band_usage(usage, 0, 100) * 0.03 + \
        within_band_usage(usage, 100, 200) * 0.05 + \
        within_band_usage(usage, 200, math.inf) * 0.07


if __name__ == "__main__":
    print(f"Base Charge: ${base_charge(80)}")

    print(f"Base Charge: ${base_charge_refactored(80)}")
