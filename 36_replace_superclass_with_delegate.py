# Replace Superclass with Delegate

from typing import List


class CatalogItem:

    def __init__(self, id: int, title: str, tags: List[str]) -> None:
        self._id = id
        self._title = title
        self._tags = tags

    def has_tag(self, tag: str) -> bool:
        return tag in self._tags


class Scroll(CatalogItem):
    """ This is not a good model, because a scroll that refers to a unique catalog item may have several copies """

    def __init__(self, id: int, title: str, tags: List[str], date_last_cleaned: int) -> None:
        super().__init__(id, title, tags)
        # Pretend date is an integer for simplicity
        self._last_cleaned = date_last_cleaned

    def needs_cleaning(self, target_date: int) -> bool:
        threshold = 700 if self.has_tag('revered') else 1500
        return target_date - self._last_cleaned > threshold


"""
One of the class examples of mis-inheritance from the early days of object 
oriented programming was making a stack a subclass of a list. The problem with
this is that all operations of a list were part of the interface of the stack,
but most of them were not applicable to a stack.

If functions of a superclass do not make sense on the subclass, that's a sign 
that inheritance shouldn't have been used. Using delegation makes it clear
that the class is a separate entity, with far less coupling than that of 
a parent-child relationship.
"""


class Scroll_:

    def __init__(self, id: int, title: str, tags: List[str], date_last_cleaned: int) -> None:
        self._catalog_item = CatalogItem(id, title, tags)
        # Pretend date is an integer for simplicity
        self._last_cleaned = date_last_cleaned

    def needs_cleaning(self, target_date: int) -> bool:
        threshold = 700 if self.has_tag('revered') else 1500
        return target_date - self._last_cleaned > threshold

    def has_tag(self, tag: str) -> bool:
        return self._catalog_item.has_tag(tag)


if __name__ == "__main__":
    scroll = Scroll(id=1234, title="Refactoring", tags=[
                    "coding", "revered"], date_last_cleaned=10)
    print(f"Needs cleaning: {scroll.needs_cleaning(target_date=2000)}")

    scroll1 = Scroll_(id=1234, title="Refactoring", tags=[
                      "coding", "revered"], date_last_cleaned=10)
    print(f"Needs cleaning: {scroll1.needs_cleaning(target_date=2000)}")

    scroll1_copy = Scroll_(id=1234, title="Refactoring", tags=[
                           "coding", "revered"], date_last_cleaned=1500)
    print(f"Needs cleaning: {scroll1_copy.needs_cleaning(target_date=2000)}")
