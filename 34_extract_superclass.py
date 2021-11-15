# Extract Superclass
from typing import List


class Employee:

    def __init__(self, id: int, name: str, monthly_cost: float) -> None:
        self._id = id
        self._name = name
        self._monthly_cost = monthly_cost

    @property
    def monthly_cost(self):
        return self._monthly_cost

    @property
    def annual_cost(self):
        return 12 * self.monthly_cost


class Department:

    def __init__(self, name: str, monthly_costs: List[float]) -> None:
        self._name = name
        self._monthly_costs = monthly_costs

    @property
    def monthly_cost(self):
        return sum(self._monthly_costs)

    @property
    def annual_cost(self):
        return 12 * self.monthly_cost


"""
If two classes are doing similar things, we can take advantage of the basic
mechanism of inheritance and pull the similarities up into a superclass.

Many programmers treat inheritance as something that should be carefully 
planned in advance, based on some kind of classification structure in the
real world, but this structure can also be realized as a program
evolves.
"""


class Party:

    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def monthly_cost(self):
        raise NotImplementedError

    @property
    def annual_cost(self):
        return 12 * self.monthly_cost


class Employee_(Party):

    def __init__(self, id: int, name: str, monthly_cost: float) -> None:
        super().__init__(name)
        self._id = id
        self._monthly_cost = monthly_cost

    @property
    def monthly_cost(self):
        return self._monthly_cost


class Department_(Party):

    def __init__(self, name: str, monthly_costs: List[float]) -> None:
        super().__init__(name)
        self._monthly_costs = monthly_costs

    @property
    def monthly_cost(self):
        return sum(self._monthly_costs)


if __name__ == "__main__":
    emp = Employee(123, "varun", 10)
    dep = Department("engineering", [10, 20, 30])
    print(f"Employee annual cost: {emp.annual_cost}")
    print(f"Department annual cost: {dep.annual_cost}")

    emp = Employee_(123, "varun", 10)
    dep = Department_("engineering", [10, 20, 30])
    print(f"Employee annual cost: {emp.annual_cost}")
    print(f"Department annual cost: {dep.annual_cost}")
