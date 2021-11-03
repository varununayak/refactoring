# Extract Class

class Person:

    def __init__(self, name: str, office_area_code: int, office_number: int) -> None:
        self.name = name
        self.office_area_code = office_area_code
        self.office_number = office_number

    @property
    def telephone_number(self) -> str:
        return f"({self.office_area_code})-{self.office_number}"


"""
Classes can sometimes get very big, affecting readability and complicated to add more features too.
At such a time it makes sense to split the class into two (or more) classes..
A good sign that the class can be split is when a subset of the data and a subset of the methods
go together, or subsets of data change together or are particularly dependent on each other.
Good abstractions help reveal these separations.

Note: The opposite of extract class, known as inline class is done when one class is too small or 
can be absorbed into another, in which case all its functionality is moved into the target class and the
class that is not required is removed.
"""


class TelephoneNumber:

    def __init__(self, office_area_code: int, office_number: int) -> None:
        self.office_area_code = office_area_code
        self.office_number = office_number

    def __repr__(self) -> str:
        return f"({self.office_area_code})-{self.office_number}"


class Person2:

    def __init__(self, name: str, office_area_code: int, office_number: int) -> None:
        self.name = name
        self.telephone_number = TelephoneNumber(
            office_area_code, office_number)


if __name__ == "__main__":
    p1 = Person("Varun", 650, 111111)
    print(f"Phone number of {p1.name} is {p1.telephone_number}")
    p2 = Person2("Varun", 650, 111111)
    print(f"Phone number of {p2.name} is {p2.telephone_number}")