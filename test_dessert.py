import pytest
from dessert import DessertItem, Candy


class DummyDessert(DessertItem):
    def calculate_cost(self) -> float:
        return 0.0


def test_dessert_item_default():
    item = DummyDessert()
    assert item.name == ""
    assert item.tax_percent == 7.25
    assert item.packaging is None


def test_dessert_item_provided():
    item = Candy("Generic Dessert")
    assert item.name == "Generic Dessert"


def test_dessert_item_updated():
    item = DummyDessert("Generic Dessert")
    item.name = "Updated Dessert"
    item.tax_percent = 8.0
    item.packaging = "Wrapper"
    assert item.name == "Updated Dessert"
    assert item.tax_percent == 8.0
    assert item.packaging == "Wrapper"


def test_dessert_item_tax():
    item = Candy("Test", 1.0, 100.0)
    assert item.calculate_cost() == 100.0
    assert item.calculate_tax() == 7.25