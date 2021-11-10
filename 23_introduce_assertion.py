# Introduce Assertion

def calculate_discounted_price(original_price: float, discount_rate: float) -> float:
    discount = discount_rate * original_price
    return original_price - discount


"""
Certain sections of code only work if certain conditions are true. 
An assertion is a conditional statement that is assumed to be always true. If the
assertion fails, it indicates a programmer error.

Assertions are also good to inform the reader of the assumed state of the 
program at a particular point in the execution - a good form of communication

We should not use assertions to check for conditions that you THINK are true.
They should check for conditions that NEED to be true. Assertions should only
be used to catch programmer errors, assertions on external sources of data can be dangerous.
"""


def calculate_discounted_price_assert(original_price: float, discount_rate: float) -> float:
    assert 0 <= discount_rate < 1, "Discount rate must be in range [0, 1)"
    discount = discount_rate * original_price
    return original_price - discount


if __name__ == "__main__":
    print(f"Discounted price: {calculate_discounted_price(100, 0.2)}")
    print(f"Discounted price: {calculate_discounted_price_assert(100, 0.2)}")
