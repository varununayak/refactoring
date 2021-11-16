# Split Phase

class ShippingMethod:

    def __init__(self, discounted_fee: float, discount_threshold: float, fee_per_case: float) -> None:
        self.discounted_fee = discounted_fee
        self.discount_threshold = discount_threshold
        self.fee_per_case = fee_per_case


class Product:

    def __init__(self, base_price: float, discount_threshold: float, discount_rate: float) -> None:
        self.base_price = base_price
        self.discount_threshold = discount_threshold
        self.discount_rate = discount_rate


def price_order(product: Product, quantity: int, shipping_method: ShippingMethod) -> float:
    base_price = product.base_price * quantity
    discount = max(quantity - product.discount_threshold, 0) + \
        product.base_price * product.discount_rate
    shipping_per_case = shipping_method.discounted_fee if base_price > shipping_method.discount_threshold else shipping_method.fee_per_case
    shipping_cost = quantity * shipping_per_case
    return base_price - discount + shipping_cost


"""
When we see code dealing with two or more different things, there is an opportunity to split them
into different modules / functions that are sequentially called. Each step will be significantly 
different from the others. The best clue that the code needs this refactoring is when different 
stages of the code fragment operate on different sets of data and functions.
"""

# Create an intermediate data structure for price data


class PriceData:

    def __init__(self, base_price, quantity, discount) -> None:
        self.base_price = base_price
        self.quantity = quantity
        self.discount = discount


def calculate_price_data(product: Product, quantity: int) -> PriceData:
    base_price = product.base_price * quantity
    discount = max(quantity - product.discount_threshold, 0) + \
        product.base_price * product.discount_rate
    return PriceData(base_price, quantity, discount)


def apply_shipping(price_data: PriceData, shipping_method: ShippingMethod) -> float:
    shipping_per_case = shipping_method.discounted_fee if price_data.base_price > shipping_method.discount_threshold else shipping_method.fee_per_case
    shipping_cost = price_data.quantity * shipping_per_case
    return price_data.base_price - price_data.discount + shipping_cost


def price_order_refactored(product: Product, quantity: int, shipping_method: ShippingMethod) -> float:
    # Divide into two phases: product pricing and shipping
    price_data = calculate_price_data(product, quantity)
    return apply_shipping(price_data, shipping_method)


if __name__ == "__main__":
    print(
        f"Price: {price_order(Product(100, 500, 10), 100, ShippingMethod(25, 200, 2))}")
    print(
        f"Price: {price_order_refactored(Product(100, 500, 10), 100, ShippingMethod(25, 200, 2))}")
