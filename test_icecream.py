import pytest
from dessert import IceCream


def test_icecream_default():
    ic = IceCream()
    assert ic.name == ""
    assert ic.scoop_count == 0
    assert ic.price_per_scoop == 0.0
    assert ic.packaging == "Bowl"


def test_icecream_provided():
    ic = IceCream("Pistachio", 2, 1.50)
    assert ic.name == "Pistachio"
    assert ic.scoop_count == 2
    assert ic.price_per_scoop == 1.50
    assert ic.packaging == "Bowl"


def test_icecream_updated():
    ic = IceCream("Pistachio", 2, 1.50)
    ic.name = "Vanilla"
    ic.scoop_count = 3
    ic.price_per_scoop = 2.00
    ic.packaging = "Cone"
    assert ic.name == "Vanilla"
    assert ic.scoop_count == 3
    assert ic.price_per_scoop == 2.00
    assert ic.packaging == "Cone"


def test_icecream_cost_and_tax():
    ic = IceCream("Pistachio", 2, 0.79)
    assert ic.calculate_cost() == 1.58
    assert ic.calculate_tax() == 0.11