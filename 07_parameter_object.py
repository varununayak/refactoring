# Introduce Parameter Object

from typing import Tuple


def readings_within_range(readings: Tuple[float], min: float, max: float) -> bool:
    return all([reading < max and reading > min for reading in readings])


"""
Data items that regularly travel together, appearing in function after function are known as a 
data clump. Such data clumps are best replaced with a single data structure.

The process can also improve the conceptual picture of the code, raising the data structures
as new abstractions that can greatly simplify the understanding of the domain of the code.
"""


class Range:

    def __init__(self, min: float, max: float) -> None:
        self.min = min
        self.max = max


def readings_within_range_refactored(readings: Tuple[float], range: Range) -> bool:
    return all([reading < range.max and reading > range.min for reading in readings])


"""
Making the range a class makes it easier to move functionality into the class itself if required
"""


class RangeBetter:

    def __init__(self, min: float, max: float) -> None:
        self.min = min
        self.max = max

    def within_range(self, value: float) -> bool:
        return value > self.min and value < self.max


if __name__ == "__main__":
    readings = (24, 12, 2, 10)
    print(f"Within range: {readings_within_range(readings, 0, 20)}")
    print(
        f"Within range: {readings_within_range_refactored(readings, Range(0, 20))}")
    range = RangeBetter(0, 20)
    print(
        f"Within range: {all([range.within_range(reading) for reading in readings])}")
