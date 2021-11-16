# Replace Type Code with Subclasses

from typing import Match, NamedTuple


class Employee:

    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type
        Employee._validate_type(type)

    @staticmethod
    def _validate_type(type: str):
        if type not in {"engineer", "salesman", "manager"}:
            raise ValueError(f"Employee type {type} not supported!")

    def __repr__(self) -> str:
        return f"Employee Name {self.name}. Type: {self.type}"


def make_employee(name: str, type: type):
    return Employee(name, type)


"""
Software systems often need to represent different kinds of similar objects.
The first tool to handle this could be some kind of type code field, like
a string or an enum. Most of the time, this type code is all we need.
However, if we find ourself writing many conditional statements based on 
the value of the type code field, it may be time to create individual
subclasses to subsume this behavior. This also implies that we are
replacing the conditionals with polymorphism - a useful refactoring technique.

The inverse of this is removing subclasses and replacing them with fields.
A subclass that does too little incurs a cost in understanding that is no longer
worthwhile. When that time comes, it's best to remove the subclass, replacing it
with a field on its superclass.
"""


class Employee_:

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Employee Name {self.name}. Type: {self.type}"


class Engineer(Employee_):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "engineer"


class Salesman(Employee_):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "salesman"


class Manager(Employee_):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "manager"


def make_employee_(name: str, type: type) -> Employee:
    # TODO(vn): Replace strings with Enum, much less error prone :)
    if type == "engineer":
        return Engineer(name)
    elif type == "salesman":
        return Salesman(name)
    elif type == "manager":
        return Manager(name)
    else:
        raise ValueError(f"Employee type {type} not supported!")


if __name__ == "__main__":
    engineer = make_employee("Varun", type="engineer")
    print(f"Let's welcome our newest engineer -> {engineer}")

    engineer = make_employee_("Varun", type="engineer")
    print(f"Let's welcome our newest engineer -> {engineer}")
