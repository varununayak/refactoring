# Inline Variable

class Order:

    def __init__(self) -> None:
        self.base_price = 10


def expensive_base(order: Order) -> bool:
    base_price = order.base_price
    return base_price > 1000

"""
Sometimes the name of a variable that is declared before an expression doesn't really communicate more than
the expression itself. In this case we can inline the variable
We need to make sure that the right hand side of the assignment does not have any side effects
"""

def expensive_base_refactored(order: Order)-> bool:
    return order.base_price > 1000


if __name__ == "__main__":
    print(f"Expensive?: {expensive_base(Order())}")
    print(f"Expensive?: {expensive_base_refactored(Order())}")