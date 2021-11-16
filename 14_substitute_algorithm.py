# Substitute Algorithm

from typing import List


def find_person(people: List[str]) -> str:
    for person in people:
        if person == "Don":
            return "Don"
        if person == "John":
            return "John"
    return ""


"""
There are often times more than one way to carry out the same logic/algorithm.
We can find clearer ways to do the same thing, or can find libraries that supplies
features that duplicate the existing code.
"""


def find_person_2(people: List[str]) -> str:
    return next((x for x in people if x in {"Don", "John"}), "")


if __name__ == "__main__":
    print(f'Found: {find_person(["Jay", "Kay", "John", "Don"])}')
    print(f'Found: {find_person(["Jay", "Kay"])}')

    print(f'Found: {find_person_2(["Jay", "Kay", "John", "Don"])}')
    print(f'Found: {find_person_2(["Jay", "Kay"])}')
