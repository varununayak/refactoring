# Extract Variable

class Order:

    def __init__(self) -> None:
        self.quantity = 3
        self.item_price = 30


def price(order: Order):
    return order.quantity * order.item_price - max(0, order.quantity - 500) * order.item_price * 0.05 + min(100, order.quantity * order.item_price * 0.1)

"""
NOTES:

Variables give us the ability to name a part of a more complex piece of logic
If we want to extract an expression, we should ensure it has no side effects.
"""

def price_refactored(order: Order):
    base_price = order.quantity * order.item_price
    shipping = min(base_price * 0.1, 100)
    discount_based_on_quantity = max(
        0, order.quantity - 500) * order.item_price * 0.05
    return base_price - discount_based_on_quantity + shipping

"""
Can also be refactored to be made a part of the class itself.
This is ideal if we are generally only interested in the final price and want to hide
away ugly details within the object.
"""

class OrderImproved:

    def __init__(self) -> None:
        self.quantity = 3
        self.item_price = 30

    def base_price(self):
        return self.quantity * self.item_price
    
    def discount_based_on_quantity(self):
        return max(0, self.quantity - 500) * self.item_price * 0.05

    def shipping(self):
        return min(self.base_price() * 0.1, 100)



if __name__ == "__main__":
    print(f"Price: {price(Order())}")
    print(f"Price: {price_refactored(Order())}")
    order = OrderImproved()
    print(f"Price: {order.base_price() - order.discount_based_on_quantity() + order.shipping()}")
