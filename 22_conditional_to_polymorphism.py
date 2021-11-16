# Replace Conditional with Polymorphism

class Bird:

    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type


def airspeed(bird: Bird) -> float:
    if bird.type == "AfricanSwallow":
        return 10
    elif bird.type == "BlueParrot":
        return 20
    else:
        return 15


"""
It is always better to add more structure to conditional logic to make it easier
to reason about. Using classes and polymorphism can make this structure very
explicit. 

A common case for this is when a set of types can handle the conditional logic
differently. The most obvious case is when there is switch statement checking
for type.
"""


class BirdBase:

    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def airspeed(self) -> float:
        return 15


class AfricanSwallow(BirdBase):

    @property
    def airspeed(self) -> float:
        return 10


class BlueParrot(BirdBase):

    @property
    def airspeed(self) -> float:
        return 20


if __name__ == "__main__":
    print(f'Airspeed = {airspeed(Bird("varun", "AfricanSwallow"))}')
    bird = AfricanSwallow("varun")
    print(f"Airspeed = {bird.airspeed}")
