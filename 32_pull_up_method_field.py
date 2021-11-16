# Pull Up Method or Field


class Party:

    def __init__(self) -> None:
        pass


class Employee(Party):

    def __init__(self, name: str, monthly_cost: float) -> None:
        super().__init__()
        self.name = name
        self.monthly_cost = monthly_cost

    @property
    def annual_cost(self) -> float:
        return self.monthly_cost * 12


class Department(Party):

    def __init__(self, group: int, monthly_cost: float) -> None:
        super().__init__()
        self.group = group
        self.monthly_cost = monthly_cost

    @property
    def total_annual_cost(self) -> float:
        return self.monthly_cost * 12


"""
Eliminating duplicated code is important. They may work fine today but they are
breeding grounds for massive bugs. When similar/identical methods exist in
all subclasses, it is a clear indicator that the method can be extracted to the
superclass. This can also be done for fields as well as common elements of
special methods like the constructor of a class.

The inverse of this i.e. pushing down fields or methods is also a refactoring technique
that is employed when the methods fields in a superclass are ONLY used by ONE subclass.
"""


class Party2:

    def __init__(self, monthly_cost: float) -> None:
        self.monthly_cost = monthly_cost

    @property
    def annual_cost(self) -> float:
        return self.monthly_cost * 12


class Employee2(Party2):

    def __init__(self, name: str, monthly_cost: float) -> None:
        super().__init__(monthly_cost)
        self.name = name


class Department2(Party2):

    def __init__(self, group: int, monthly_cost: float) -> None:
        super().__init__(monthly_cost)
        self.group = group

    @property
    def total_annual_cost(self) -> float:
        # For backwards compatibility
        print(f"** total_annual_cost will be depecrated soon. Please use annual_cost. **")
        return super().annual_cost


if __name__ == "__main__":
    emp = Employee("Varun", 20)
    dep = Department(1, 100)
    print(f"Employee {emp.name} annual cost: {emp.annual_cost}")
    print(f"Department {dep.group} annual cost: {dep.total_annual_cost}")

    emp2 = Employee2("Varun", 20)
    dep2 = Department2(1, 100)
    print(f"Employee {emp2.name} annual cost: {emp2.annual_cost}")
    print(f"Department {dep2.group} annual cost: {dep2.total_annual_cost}")
