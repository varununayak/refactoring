# Combine functions into class

class Order:

    def __init__(self, item_price: float, quantity: int) -> None:
        self.item_price = item_price
        self.quantity = quantity


def tax_from_order(order: Order, tax_threshold: float = 10.0, tax_percentage: float = 15.0) -> float:
    base = base_price(order.item_price, order.quantity)
    taxable_charge = max(0, base - tax_threshold)
    return taxable_charge * tax_percentage / 100


def base_price(item_price: float, quantity: int) -> float:
    return item_price * quantity


"""
When a group of functions operate closely together on a common body of data, there is an 
opportunity to refactor the methods + data into a class. Using a class makes the common
environment in which the methods are operating more explicit and lends itself to better
encapsulation frin clients
"""


class OrderBetter:

    def __init__(self, item_price: float, quantity: int, tax_percentage: float = 15.0, tax_threshold: float = 10.0) -> None:
        self.item_price = item_price
        self.quantity = quantity
        self.tax_percentage = tax_percentage
        self.tax_threshold = tax_threshold

    @property
    def base_price(self):
        """ Calculated on demand """
        return self.item_price * self.quantity

    @property
    def taxable_charge(self):
        """ Calculated on demand """
        return max(0, self.base_price - self.tax_threshold)

    @property
    def tax(self):
        """ Calculated on demand """
        return self.taxable_charge * self.tax_percentage / 100


if __name__ == "__main__":
    print(f"Tax: ${tax_from_order(Order(3, 20))}")
    order = OrderBetter(3, 20)
    print(f"Tax: ${order.tax}")
