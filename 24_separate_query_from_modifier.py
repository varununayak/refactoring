# Separate Query from Modifier

from typing import Optional, List


def set_off_alarms():
    print("BEE BOO")


def alert_for_miscreant(people: List[str]):
    for person in people:
        if person in {"John", "Bob"}:
            set_off_alarms()
            return person
    return None


"""
A function that gives back a value and has no side effects is very valuable.
This function can be called as much as we like and we have nothing to worry about.

A good rule to follow is to separate functions that return values and those that
have side effects - the command-query separation that is treated as a rule
by most programmers.
"""


def find_miscreant(people: List[str]) -> Optional[str]:
    for person in people:
        if person in {"John", "Bob"}:
            return person
    return None


def alert_for_miscreant_refactored(people: List[str]) -> Optional[str]:
    miscreant = find_miscreant(people)
    if miscreant is not None:
        set_off_alarms()
    return miscreant


if __name__ == "__main__":
    print(f"Alert for miscreant: {alert_for_miscreant(['Harry', 'Bob'])}")
    print(
        f"Alert for miscreant: {alert_for_miscreant_refactored(['Harry', 'Bob'])}")
