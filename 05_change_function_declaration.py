# Change function declaration

class Address:

    def __init__(self, state) -> None:
        self.state = state


class Customer:

    def __init__(self, address: Address) -> None:
        self.address = address


def in_new_england(customer: Customer) -> bool:
    return customer.address.state in {"MA", "CT", "ME", "VT", "NH", "RI"}


"""
Changing function declaration could mean one of two things:
1) Changing function name
2) Changing the signature of the function (adding/removing/changing arguments)

A good function name + signature is when you don't need to keep looking at the body to remind 
yourself what the function does. A good inspiration for function name are the comments about
what the function does.
There is no right answer when it comes to whether the function only needs the lowest level
object (state) or the larger object (Customer). THe former provides maximal decoupling between
object and function but the later leaves room for flexibility in the future.
"""

# Updated name and signature to only require state and not entire customer class


def state_in_new_england(state: str) -> bool:
    return state in {"MA", "CT", "ME", "VT", "NH", "RI"}


if __name__ == "__main__":
    print(f"In New England: {in_new_england(Customer(Address('CT')))}")
    print(f"In New England: {state_in_new_england('CT')}")
