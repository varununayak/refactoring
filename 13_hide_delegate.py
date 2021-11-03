# Hide Delegate

class Department:

    def __init__(self, manager: str, charge_code: int) -> None:
        self.manager = manager
        self.charge_code = charge_code


class Person:

    def __init__(self, name: str, manager: str, charge_code: int) -> None:
        self.name = name
        self.department = Department(manager, charge_code)


"""
One of the keys to good modular design is encapsulation. Encapsulation means that modules need to know
less about other parts of the system. Therefore, when changes occur in one module, fewer other modules 
are affected by the changes.

For e.g. if a client needs to access a delegate object in a server, and the delegate object requires some
changes, both the server and the client will be affected if the delegate is called directly by the client

Note: The opposite of this is called "remove middle man". There is price for adding methods that hide 
the delegate, and after a point, the class that holds the delegate is almost like a "middle man",
in which case perhaps it is better for the client to call the delegate class directly.

It can be hard to figure out what the right amount of hiding is, fortunately with "hide delegate" 
and "remove middle man" we can keep refactoring to maintain the balance given the stage of the code base.
"""


class Department2:

    def __init__(self, manager: str, charge_code: int) -> None:
        self.manager = manager
        self.charge_code = charge_code


class Person2:

    def __init__(self, name: str, manager: str, charge_code: int) -> None:
        self.name = name
        self._department = Department(manager, charge_code)

    @property
    def manager(self):
        return self._department.manager


if __name__ == "__main__":
    p1 = Person("Varun", "Akshay", 1234)
    print(f"Person {p1.name} manager: {p1.department.manager}")
    p2 = Person2("Varun", "Akshay", 1234)
    print(f"Person {p2.name} manager: {p2.manager}")
