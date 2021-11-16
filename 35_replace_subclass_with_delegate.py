# Replace subclass with delegate

from typing import NamedTuple


class Show(NamedTuple):
    price: float


class Extras(NamedTuple):
    premium_fee: float = 20
    dinner: bool = False


class Booking:

    def __init__(self, show: Show, date: str) -> None:
        self._show = show
        self._date = date

    def is_peak_day(self) -> bool:
        # Omit peak day logic here for brevity
        return True

    @property
    def base_price(self) -> float:
        return self._show.price * 1.15 if self._is_peak_day else self._show.price


class PremiumBooking(Booking):

    def __init__(self, show: Show, date: str, extras: Extras) -> None:
        super().__init__(show, date)
        self._extras = extras

    @property
    def base_price(self) -> float:
        return self._show.price + self._extras.premium_fee

    def has_dinner(self) -> bool:
        return self._extras.dinner and not self._is_peak_day()


"""
If we have some objects whose behavior varies from category to category, the natural
mechanism to express this is by using inheritance.

But, inheritance has its downsides. Most obviously, it's a card that can be played only once
i.e. if there is more than one reason to vary something, we can only use one axis
of variation in the inheritance hierarchy. For example, if we want to vary the
class "Person" based on both age and income level, we can only have inheritance over
either one of the two traits, not both.

Another issue with inheritance is that it introduces a very close relationship 
between parent and child. Changes to either class can easily break the other.
Delegation reduces the coupling between classes.

There is a saying that goes "Favor object composition over inheritance", however, it is 
better to observe "Favor a judicious mixture of composition and inheritance over
either alone".

"""


class Booking_:

    def __init__(self, show: Show, date: str, extras: Extras = None) -> None:
        self._show = show
        self._date = date
        if extras is not None:
            self._premium_delegate = PremiumBookingDelegate(show, extras)
        else:
            self._premium_delegate = None

    def is_peak_day(self) -> bool:
        # Omit peak day logic here for brevity
        return True

    @property
    def base_price(self) -> float:
        if self._premium_delegate:
            return self._premium_delegate.base_price
        else:
            return self._show.price * 1.15 if self._is_peak_day else self._show.price

    def has_dinner(self) -> bool:
        if self._premium_delegate is None:
            raise NotImplementedError
        return self._premium_delegate.has_dinner() and not self._is_peak_day()


class PremiumBookingDelegate():

    def __init__(self, show: Show, extras: Extras) -> None:
        self._show = show
        self._extras = extras

    @property
    def base_price(self) -> float:
        return self._show.price + self._extras.premium_fee

    def has_dinner(self) -> bool:
        return self._extras.dinner


if __name__ == "__main__":
    pb = PremiumBooking(Show(price=100), "01/20/2020", Extras())
    print(f"Premium Booking base price: {pb.base_price}")

    pb = Booking_(Show(price=100), "01/20/2020", Extras())
    print(f"Premium Booking base price: {pb.base_price}")
