# Replace Constructor with Factory Function


class Employee:

    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    def __repr__(self) -> str:
        return f"Employee Name: {self.name}.\nType: {self.type}"


"""
Object oriented languages have constructor functions (special methods)
that are called to initialize an object. Constructor naming is fixed,
which means we cannot use any name that is clearer than the default.
In some languages, special keywords might be required to invoke the constructor.
"""


def make_engineer(name):
    return Employee(name, type="engineer")


if __name__ == "__main__":
    engineer_1 = Employee("Varun", 'engineer')
    print(f"Created engineer:\n{engineer_1}\n")
    engineer_2 = make_engineer(name="Varun")
    print(f"Created engineer:\n{engineer_2}\n")
