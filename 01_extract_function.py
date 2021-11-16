# Extract Function

"""
Function to print how much a customer owes based on an invoice
"""

from datetime import datetime
from typing import List


class Order:
    def __init__(self, amount: float) -> None:
        self.amount = amount


class Invoice:
    def __init__(self, orders: List[Order], customer: str, due_date=None) -> None:
        self.orders = orders
        self.customer = customer
        self.due_date = due_date


def print_owing(invoice: Invoice):
    outstanding = 0

    print("*************************")
    print("***** Customer Owes *****")
    print("*************************")

    for order in invoice.orders:
        outstanding += order.amount

    today = datetime.now()
    invoice.due_date = today

    print(f"Name: {invoice.customer}")
    print(f"Amount: {outstanding}")
    print(f"Due: {invoice.due_date}")


"""
Optimizing compilers often work better with shorter functions that can be cached more easily.
Small functions work only if the names are good.
Name a function by its intent, not by what it actually does. There is no pressure to come up with the best name right away.
"""


def print_banner():
    print("*************************")
    print("***** Customer Owes *****")
    print("*************************")


def calculate_outstanding(invoice: Invoice) -> float:
    outstanding = 0
    for order in invoice.orders:
        outstanding += order.amount
    return outstanding


def print_details(invoice, outstanding):
    print(f"Name: {invoice.customer}")
    print(f"Amount: {outstanding}")
    print(f"Due: {invoice.due_date}")


def record_due_date(invoice: Invoice):
    today = datetime.now()
    invoice.due_date = today


def print_owing_refactored(invoice: Invoice):
    print_banner()
    outstanding = calculate_outstanding(invoice)
    record_due_date(invoice)
    print_details(invoice, outstanding)


if __name__ == "__main__":
    invoice = Invoice(orders=[Order(10), Order(20)], customer="Varun")
    print_owing(invoice)
    print_owing_refactored(invoice)
