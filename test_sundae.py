import pytest
from dessert import Sundae


def test_sundae_default():
    s = Sundae()
    assert s.name == ""
    assert s.scoop_count == 0
    assert s.price_per_scoop == 0.0
    assert s.topping_name == ""
    assert s.topping_price == 0.0
    assert s.packaging == "Boat"


def test_sundae_provided():
    s = Sundae("Vanilla", 2, 1.50, "Hot Fudge", 0.99)
    assert s.name == "Vanilla"
    assert s.scoop_count == 2
    assert s.price_per_scoop == 1.50
    assert s.topping_name == "Hot Fudge"
    assert s.topping_price == 0.99
    assert s.packaging == "Boat"


def test_sundae_updated():
    s = Sundae("Vanilla", 2, 1.50, "Hot Fudge", 0.99)
    s.name = "Chocolate"
    s.scoop_count = 3
    s.price_per_scoop = 2.00
    s.topping_name = "Caramel"
    s.topping_price = 1.25
    s.packaging = "Cup"
    assert s.name == "Chocolate"
    assert s.scoop_count == 3
    assert s.price_per_scoop == 2.00
    assert s.topping_name == "Caramel"
    assert s.topping_price == 1.25
    assert s.packaging == "Cup"


def test_sundae_cost_and_tax():
    s = Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)
    assert s.calculate_cost() == 3.36
    assert s.calculate_tax() == 0.24