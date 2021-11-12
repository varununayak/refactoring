# Replace Query with Parameter

class Thermostat:

    def __init__(self) -> None:
        self.selected_temperature = 25
        self.current_temperature = 30


thermostat = Thermostat()


class HeatingPlan:

    def __init__(self, low, high) -> None:
        self.low = low
        self.high = high

    def target_temperature(self):
        if thermostat.selected_temperature > self.high:
            return self.high
        elif thermostat.selected_temperature < self.low:
            return self.low
        else:
            return thermostat.selected_temperature


def control_temperature(plan: HeatingPlan):
    if plan.target_temperature() > thermostat.current_temperature:
        return "HEATING"
    elif plan.target_temperature() < thermostat.current_temperature:
        return "COOLING"
    else:
        return "OFF"


"""
When looking through a function's body, we may see references to objects that were
not part of the parameter list, likely a global object. 

It is generally easier to reason about a function that will always give the same result
when called with the same parameter values. This is called referential transparency.
Although shifting the referenced object to the parameter list puts the burden on the caller
to pass this in, there is often a lot gained just by doing that and ensuring 
referential transparency.

"""


class HeatingPlanBetter:

    def __init__(self, low, high) -> None:
        self.low = low
        self.high = high

    def target_temperature(self, selected_temperature: float):
        """
        Now, everytime target_temperature() is called it is guaranteed
        to give the same result for the same value of selected temperature
        """
        if selected_temperature > self.high:
            return self.high
        elif selected_temperature < self.low:
            return self.low
        else:
            return selected_temperature


def control_temperature_refactored(plan: HeatingPlan):
    if plan.target_temperature(thermostat.selected_temperature) > thermostat.current_temperature:
        return "HEATING"
    elif plan.target_temperature(thermostat.selected_temperature) < thermostat.current_temperature:
        return "COOLING"
    else:
        return "OFF"


if __name__ == "__main__":
    plan = HeatingPlan(20, 30)
    print(f"Control Temperature Result: {control_temperature(plan)}")
    plan = HeatingPlanBetter(20, 30)
    print(
        f"Control Temperature Result: {control_temperature_refactored(plan)}")
