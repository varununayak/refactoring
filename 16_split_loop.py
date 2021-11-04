# Split Loop

import math
from typing import Tuple, List


class Person:

    def __init__(self, age: int, salary: float) -> None:
        self.age = age
        self.salary = salary


def youngest_and_total_salary(people: List[Person]) -> Tuple[int, float]:
    youngest = math.inf
    total_salary = 0
    for person in people:
        if person.age < youngest:
            youngest = person.age
        total_salary += person.salary
    return youngest, total_salary


"""
Often, loops are seen to be doing two things at once because they can do that in
one pass through the loop. But, if you are doing two different things in the same
loop, and you want to change the loop you must understand both things.

Loops that do many things need to return structures or populate local variables.
Splitting a loop can help return only one value at a time, and can lend itself
to extraction of the loop into a function that returns that value only
"""


def youngest(people: List[Person]) -> int:
    youngest = math.inf
    for person in people:
        if person.age < youngest:
            youngest = person.age
    return youngest


def total_salary(people: List[Person]) -> float:
    return sum([person.salary for person in people])


if __name__ == "__main__":
    people = [Person(24, 200), Person(50, 1000), Person(10, 0)]
    y, ts = youngest_and_total_salary(people)
    print(f"Youngest: {y}. Total Salary: {ts}")
    print(
        f"Youngest: {youngest(people)}. Total Salary: {total_salary(people)}")
