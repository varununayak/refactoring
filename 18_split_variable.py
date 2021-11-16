# Split Variable

class Scenario:

    def __init__(self, primary_force: float, secondary_force: float, mass: float, delay: float) -> None:
        self.primary_force = primary_force
        self.secondary_force = secondary_force
        self.mass = mass
        self.delay = delay


def distance_travelled(scenario: Scenario, time: float) -> float:
    """ A mass experiences a primary force and after a delay, a secondary force in addition to it.
     Compute distance travelled in given time"""
    distance = 0
    acc = scenario.primary_force / scenario.mass
    primary_time = min(time, scenario.delay)
    distance += 1/2 * acc * primary_time ** 2  # s = 1/2 a t ^2
    secondary_time = time - scenario.delay
    if secondary_time > 0:
        primary_velocity = acc * scenario.delay
        acc = (scenario.primary_force + scenario.secondary_force) / scenario.mass
        distance += primary_velocity + 1/2 * acc * \
            secondary_time ** 2  # s = ut + 1/2 a t ^2
    return distance


"""
Sometimes, a method can assign to the same variable more than once. This can get confusing
to a reader because the variable has more than once responsibility in the method i.e.
looking at the assignment statement in one place doesn't necessarily mean that that's the
value it ultimately takes during its usage.
"""


def distance_travelled_refactored(scenario: Scenario, time: float) -> float:
    """ A mass experiences a primary force and after a delay, a secondary force in addition to it.
     Compute distance travelled in given time"""
    primary_acceleration = scenario.primary_force / scenario.mass
    primary_time = min(time, scenario.delay)
    distance = 1/2 * primary_acceleration * primary_time ** 2  # s = 1/2 a t ^2
    secondary_time = time - scenario.delay
    if secondary_time > 0:
        primary_velocity = primary_acceleration * scenario.delay
        secondary_acceleration = (
            scenario.primary_force + scenario.secondary_force) / scenario.mass
        distance += primary_velocity + 1/2 * secondary_acceleration * \
            secondary_time ** 2  # s = ut + 1/2 a t ^2
    return distance


if __name__ == "__main__":
    print(
        f"Distance Travelled: {distance_travelled(Scenario(10, 20, 1, 4), 10)}")

    print(
        f"Distance Travelled: {distance_travelled_refactored(Scenario(10, 20, 1, 4), 10)}")
