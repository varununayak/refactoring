# Replace derived variable with query

from typing import List


class Adjustment:

    def __init__(self, amount: float) -> None:
        self.amount = amount


class ProductionPlan:

    def __init__(self, base_production: float) -> None:
        self._production = base_production
        self._adjustments: List[Adjustment] = []

    @property
    def production(self):
        return self._production

    def apply_adjustment(self, adjustment: Adjustment):
        self._adjustments.append(adjustment)
        self._production += adjustment.amount


"""
One of the biggest sources of problems in software is mutable data. Although we cannot
completely get rid of mutable data, it is advisable to minimize its scope. One way
to make an impact is to get rid of variables that can be calculated from another set
of source data when required. This removes the need to maintain these variables and 
the calculation also makes it clear what the meaning of the data is.

A reasonable exception to this is when the source data for the calculation is immutable
which means the result is always the same i.e. the calculated variable can be 
forced to be immutable.
"""


class ProductionPlanBetter:

    def __init__(self, base_production: float) -> None:
        self._base_production = base_production
        self._adjustments: List[Adjustment] = []

    @property
    def production(self):
        return self._base_production + sum([adj.amount for adj in self._adjustments])

    def apply_adjustment(self, adjustment: Adjustment):
        self._adjustments.append(adjustment)


if __name__ == "__main__":
    pp = ProductionPlan(10)
    pp.apply_adjustment(Adjustment(5))
    print(f"Production: {pp.production}")
    ppb = ProductionPlanBetter(10)
    ppb.apply_adjustment(Adjustment(5))
    print(f"Production: {ppb.production}")
