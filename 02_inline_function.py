# Inline Function

class Driver:

    def __init__(self) -> None:
        self.num_late_deliveries = 4


def rating(driver: Driver) -> int:
    return 1 if more_than_five_late_deliveries(driver) else 2


def more_than_five_late_deliveries(driver: Driver) -> bool:
    return driver.num_late_deliveries > 5


def rating_refactored(driver : Driver) -> int:
    return 1 if driver.num_late_deliveries > 5 else 2



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


if __name__ == "__main__":
    print(f"Rating: {rating(Driver())}")
    print(f"Rating: {rating_refactored(Driver())}")
