# Encapsulate Variable

from typing import Dict


default_owner_ = {"FirstName": "Varun", "LastName": "Nayak"}


"""
Refactoring data can be challenging when compared to refactoring functions since all the 
references to the data must be changed in a single cycle to keep the code working.
As the scope of access of the data grows, the refactoring gets exponentially more
complicated. This is why global data is a pain to manage.

Creating encapsulating functions to access and update the variables in question help 
enforce access control.
"""

default_owner_data = {"FirstName": "Varun", "LastName": "Nayak"}


def default_owner() -> Dict:
    """ Getter function """
    # Better to return copy of data to ensure that references cannot be modified accidentally
    return default_owner_data.copy()


def set_default_owner(new_owner: Dict):
    """ Setter function """
    global default_owner_data
    default_owner_data = new_owner.copy()


if __name__ == "__main__":
    print(f"Default owner: {default_owner()}")
    print(f"Setting default owner to Akshay Nayak")
    set_default_owner({"FirstName": "Akshay", "LastName": "Nayak"})
    print(f"Default owner: {default_owner()}")
