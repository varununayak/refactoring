# Decompose and Consolidate Conditional

from enum import IntEnum


class Month(IntEnum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12


SUMMER_CHARGE = 10


class Date:

    def __init__(self, month: Month, day: int, year: int) -> None:
        self.month = month
        self.day = day
        self.year = year
        # TODO: Add a validator method during init to check if date is valid


def charge(date: Date) -> float:
    charge = 0
    # Some Code
    # ..
    if (date.month in {Month.JUL, Month.AUG}):
        charge += SUMMER_CHARGE
    if (date.month == Month.JUN and date.day >= 15):
        charge += SUMMER_CHARGE
    if (date.month == Month.SEP and date.day < 15):
        charge += SUMMER_CHARGE
    # Some Code
    # ..
    return charge


"""
The most common source of complexity in software is complex conditional logic.
The computation of the truth of the condition can be complex, and such complexity 
can hurt the reader when trying to understand the consequence (action taken)
based on the result of the condition.

The intention can be made clear by replacing the chunk of code that evaluates the
condition to a function.
"""


class Date2:

    def __init__(self, month: Month, day: int, year: int) -> None:
        self.month = month
        self.day = day
        self.year = year
        # TODO: Add a validator method during init to check if date is valid

    def in_summer(self) -> bool:
        return self.month in {Month.JUL, Month.AUG} or \
            (self.month == Month.JUN and self.day >= 15) or \
            (self.month == Month.SEP and self.day < 15)


def charge2(date: Date2) -> float:
    charge = 0
    # Some Code
    # ..
    if date.in_summer():
        charge += SUMMER_CHARGE
    # Some Code
    # ..
    return charge


if __name__ == "__main__":
    print(f"Charge: {charge(Date(Month.JUN, 14, 2020))}")
    print(f"Charge: {charge(Date(Month.JUL, 30, 2020))}")
    
    print(f"Charge: {charge2(Date2(Month.JUN, 14, 2020))}")
    print(f"Charge: {charge2(Date2(Month.JUL, 30, 2020))}")
