# Moving Features (Notes Only)

"""
Another important aspect of refactoring is simply moving elements between contexts.
Contexts can be functions, modules, classes, loops, etc.
"""

"""
Move Function

The most straightforward reason to move a function is when it references elements in other
contexts than the one it currently resides in.
Although it can be difficult to decide where the best place for a function is, the more 
difficult this choice the less it matters. Better to start with functions in the same
context, and move them later.
"""

"""
Move Field

The strength of a program is really founded on its data structures. I the data structures
are good and match the problem, the behavior code is generally simple. Poor data structures 
makes the behavior code messy and harder to maintain / understand. Techniques like 
domain-driven design help with coming up with appropriate data structures for a given application.
"""


"""
Move Statement into Functions

Moving statements into functions can improve readability and understanding of the source function.
Simply extracting a function, even if the only caller of the function is the source function, 
can be a valuable refactoring for many reasons. The length of the source function reduces,
and there is opportunity to take inline code and give it a meaningful name + encapsulation.

Inverse: Move Statements to Callers

Sometimes abstractions shift as code evolves, and the common behavior that was previously uniform
now needs variation in some of its calls. We can move the varying behavior out of the function to 
its callers. 

"""

#############################################################################################

PRICING_PLAN = {'per_unit': 100}

def charge_unslid():
    deserves_discount = False
    pricing_plan = PRICING_PLAN
    order = 40
    charge_per_unit = pricing_plan['per_unit']
    if order * charge_per_unit > 2000:
        deserves_discount = True
    return deserves_discount

"""
Slide Statements

Code is easier to understand when things that are related to each other appear together. A very common
case is when all variables are declated on top of the function. It is generally better to declare
the variables just before they are used. Sliding statements can also be a preparatory step for
another refactoring, most commonly the extract function refactoring.

"""

def charge_slid():
    pricing_plan = PRICING_PLAN
    charge_per_unit = pricing_plan['per_unit']
    order = 40
    deserves_discount = (order * charge_per_unit) > 2000
    return deserves_discount

if __name__ == "__main__":
    print(f"Deserves Discount: {charge_unslid()}")
    print(f"Deserves Discount: {charge_slid()}")


