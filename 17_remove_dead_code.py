# Remove Dead Code

def always_false():
    return False


def do_something():
    print("Does not matter.")


def v1():
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")
    if always_false():
        do_something()
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")


"""
Unused code is a significant burden when trying to navigate through or understand a code base.
If code is not used any more, it should be deleted. 
Version control systems can be used to dig it out later if required.
(Commenting out code was once a common habit, when version control systems did not 
exist or were very inconvenient to use, which is not the case today)
"""


def v2():
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")
    print("Lots of code")


if __name__ == "__main__":
    v1()
    v2()
