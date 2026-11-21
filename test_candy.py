import pytest
from dessert import Candy


def test_candy_default():
    c = Candy()
    assert c.name == ""
    assert c.candy_weight == 0.0
    assert c.price_per_pound == 0.0
    assert c.packaging == "Bag"


def test_candy_provided():
    c = Candy("Candy Corn", 1.5, 2.99)
    assert c.name == "Candy Corn"
    assert c.candy_weight == 1.5
    assert c.price_per_pound == 2.99
    assert c.packaging == "Bag"


def test_candy_updated():
    c = Candy("Candy Corn", 1.5, 2.99)
    c.name = "Gummy Bears"
    c.candy_weight = 2.0
    c.price_per_pound = 3.50
    c.packaging = "Jar"
    assert c.name == "Gummy Bears"
    assert c.candy_weight == 2.0
    assert c.price_per_pound == 3.50
    assert c.packaging == "Jar"


def test_candy_cost_and_tax():
    c = Candy("Candy Corn", 1.5, 0.25)
    assert c.calculate_cost() == 0.38
    assert c.calculate_tax() == 0.03