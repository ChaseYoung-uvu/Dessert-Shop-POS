import pytest
from dessert import Cookie


def test_cookie_default():
    c = Cookie()
    assert c.name == ""
    assert c.cookie_quantity == 0
    assert c.price_per_dozen == 0.0
    assert c.packaging == "Box"


def test_cookie_provided():
    c = Cookie("Chocolate Chip", 6, 3.99)
    assert c.name == "Chocolate Chip"
    assert c.cookie_quantity == 6
    assert c.price_per_dozen == 3.99
    assert c.packaging == "Box"


def test_cookie_updated():
    c = Cookie("Chocolate Chip", 6, 3.99)
    c.name = "Oatmeal Raisin"
    c.cookie_quantity = 12
    c.price_per_dozen = 4.99
    c.packaging = "Tin"
    assert c.name == "Oatmeal Raisin"
    assert c.cookie_quantity == 12
    assert c.price_per_dozen == 4.99
    assert c.packaging == "Tin"


def test_cookie_cost_and_tax():
    c = Cookie("Chocolate Chip", 6, 3.99)
    assert c.calculate_cost() == 2.0
    assert c.calculate_tax() == 0.14