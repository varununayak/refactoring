# Preserve Whole Object

class TempRange:

    def __init__(self, low: float, high: float) -> None:
        self.low = low
        self.high = high


def is_within_range(num: float, low: float, high: float) -> bool:
    return low <= num <= high


"""
If code derives values from an object and passes the values separately to a function, we are
better off passing in the entire object itself. 
There are several advantages of doing this:
1) The code handles evolution better (no need to pass additional parameters)
2) The number of arguments is reduced
Pulling several members from an object alone to perform some logic (Feature Envy) needs a refactoring in itself
by moving that logic to a function within the object.
"""


class TempRangeBetter:

    def __init__(self, low: float, high: float) -> None:
        self.low = low
        self.high = high

    def within_range(self, temp: float) -> bool:
        return self.low <= temp <= self.high


if __name__ == "__main__":
    tr = TempRange(0, 100)
    print(f"Within Range: {is_within_range(5, tr.low, tr.high)}")

    tr = TempRangeBetter(0, 100)
    print(f"Within Range: {tr.within_range(5)}")
