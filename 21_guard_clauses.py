# Replace Nested Conditional with Guard Clauses
import random


class Employee:

    def __init__(self, retired: bool, separated: bool = False) -> None:
        self.retired = retired
        self.separated = separated


def pay_amount(employee: Employee) -> float:
    result = 0
    if employee.separated:
        raise RuntimeError("Cannot query separated employee amount")
    else:
        if employee.retired:
            result = 0
        else:
            # Some complicated logic
            complicated_logic_result = random.choice([5, 6, 10])
            # Lorem Ipsum
            result = complicated_logic_result
    return result


"""
Conditional expressions often come in one of two styles:
1) All legs of the conditional are normal behavior
2) One leg is normal but all others are unusual conditions

The intention of the code must come through in the style, so
it is better to check for the unusual cases early on in the
function and return if true. If we nest the unusual cases,
the primary purpose (if these unusual cases are not true)
get hidden in the nesting. These unusual case checks are 
called guard clauses.
"""


def pay_amount_refactored(employee: Employee) -> float:
    if employee.separated:
        raise RuntimeError("Cannot query separated employee amount")
    if employee.retired:
        return 0
    # Some complicated logic
    return random.choice([5, 6, 10])


if __name__ == "__main__":
    employee = Employee(retired=True)
    print(f"Pay Amount: {pay_amount(employee)}")

    print(f"Pay Amount: {pay_amount_refactored(employee)}")
