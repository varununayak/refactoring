# Remove Flag Argument


class Rectangle:

    def __init__(self, height: float, width: float) -> None:
        self.height = height
        self.width = width

    def get_dim(self, dim_name: str) -> float:
        if dim_name == "perimeter":
            return 2 * (self.height + self.width)
        elif dim_name == "area":
            return self.height * self.width
        else:
            return None


"""
A flag argument is an argument that the caller uses to indicate which
logic the called function should execute.

Flag arguments complicate the process of understanding what function
calls are available and how to call them. Flag arguments hide the true list of
available function calls when we read through an API document.

It is clearer to provide an explicit API for each case. Code analysis can also
now easily distinguish between different calls.
"""


class RectangleMuchBetter:

    def __init__(self, height: float, width: float) -> None:
        self.height = height
        self.width = width

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    @property
    def area(self) -> float:
        return self.width * self.height


if __name__ == "__main__":
    r1 = Rectangle(10, 20)
    print(f"Area: {r1.get_dim('area')}. Perimeter: {r1.get_dim('perimeter')}")
    
    r2 = RectangleMuchBetter(10, 20)
    print(f"Area: {r2.area}. Perimeter: {r2.perimeter}")
