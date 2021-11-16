# Replace Primitive with Object

from enum import IntEnum


def count_high_priority() -> int:
    orders = ['low', 'high', 'normal', 'rush',
              'low', 'normal', 'normal', 'high']
    high_priority_count = len(
        [order for order in orders if order in {"high", "rush"}])
    return high_priority_count


"""
During early stages of development one might prefer to use inbuilt types (primitives) such as int, str, etc.
However, as the code evolves, additional behaviors / processing might be required, which can quickly give rise
to duplicated logic. Having a class for the object instead of using a primitive gives the programmer a convenient
location to put logic specific to the needs of the class.
"""


class Priority(IntEnum):
    LOW = 0
    NORMAL = 1
    HIGH = 2
    RUSH = 3


class Order:

    def __init__(self, priority: Priority) -> None:
        self.priority = priority

    def high_priority_order(self) -> bool:
        return self.priority > Priority.NORMAL

    def __repr__(self) -> str:
        return self.priority.name


def count_high_priority_refactored() -> int:
    orders = [Order(Priority.LOW), Order(Priority.HIGH), Order(Priority.NORMAL), Order(Priority.RUSH), Order(
        Priority.LOW), Order(Priority.NORMAL), Order(Priority.NORMAL), Order(Priority.HIGH)]
    high_priority_count = len(
        [order for order in orders if order.priority > Priority.NORMAL])
    return high_priority_count


def count_high_priority_refactored_2() -> int:
    orders = [Order(Priority.LOW), Order(Priority.HIGH), Order(Priority.NORMAL), Order(Priority.RUSH), Order(
        Priority.LOW), Order(Priority.NORMAL), Order(Priority.NORMAL), Order(Priority.HIGH)]
    high_priority_count = len(
        [order for order in orders if order.high_priority_order()])
    return high_priority_count


if __name__ == "__main__":
    print(f"High priority count: {count_high_priority()}")
    print(f"High priority count: {count_high_priority_refactored()}")
    print(f"High priority count: {count_high_priority_refactored_2()}")
