# Inline Function

class Driver:

    def __init__(self, num_late_deliveries: int) -> None:
        self.num_late_deliveries = num_late_deliveries


def rating(driver: Driver) -> int:
    return 1 if more_than_five_late_deliveries(driver) else 2


def more_than_five_late_deliveries(driver: Driver) -> bool:
    return driver.num_late_deliveries > 5


"""
NOTES:

Code that uses too much indirection i.e. when it seems like every function
does simple delegation to another function, and getting lost in all the
delegation is likely, requires inlining some functions.
If the function body is as clear as the name, inlining is 
recommended.
However we don't want to inline functions that has many callers, this can
be counterproductive.
"""


def rating_refactored(driver: Driver) -> int:
    return 1 if driver.num_late_deliveries > 5 else 2


if __name__ == "__main__":
    late_driver = Driver(num_late_deliveries=4)
    print(f"Rating: {rating(late_driver)}")
    print(f"Rating: {rating_refactored(late_driver)}")
