import pytest
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

# DessertItem Tests
def test_dessert_item_default():
    item = DessertItem()
    assert item.name == ""

def test_dessert_item_provided():
    item = DessertItem("Generic Dessert")
    assert item.name == "Generic Dessert"

def test_dessert_item_updated():
    item = DessertItem("Generic Dessert")
    item.name = "Updated Dessert"
    assert item.name == "Updated Dessert"

# Candy Tests
def test_candy_default():
    c = Candy()
    assert c.name == ""
    assert c.candy_weight == 0.0
    assert c.price_per_pound == 0.0

def test_candy_provided():
    c = Candy("Candy Corn", 1.5, 2.99)
    assert c.name == "Candy Corn"
    assert c.candy_weight == 1.5
    assert c.price_per_pound == 2.99

def test_candy_updated():
    c = Candy("Candy Corn", 1.5, 2.99)
    c.name = "Gummy Bears"
    c.candy_weight = 2.0
    c.price_per_pound = 3.50
    assert c.name == "Gummy Bears"
    assert c.candy_weight == 2.0
    assert c.price_per_pound == 3.50

# Cookie Tests
def test_cookie_default():
    c = Cookie()
    assert c.name == ""
    assert c.cookie_quantity == 0
    assert c.price_per_dozen == 0.0

def test_cookie_provided():
    c = Cookie("Chocolate Chip", 6, 3.99)
    assert c.name == "Chocolate Chip"
    assert c.cookie_quantity == 6
    assert c.price_per_dozen == 3.99

def test_cookie_updated():
    c = Cookie("Chocolate Chip", 6, 3.99)
    c.name = "Oatmeal Raisin"
    c.cookie_quantity = 12
    c.price_per_dozen = 4.99
    assert c.name == "Oatmeal Raisin"
    assert c.cookie_quantity == 12
    assert c.price_per_dozen == 4.99

# IceCream Tests
def test_icecream_default():
    ic = IceCream()
    assert ic.name == ""
    assert ic.scoop_count == 0
    assert ic.price_per_scoop == 0.0

def test_icecream_provided():
    ic = IceCream("Pistachio", 2, 1.50)
    assert ic.name == "Pistachio"
    assert ic.scoop_count == 2
    assert ic.price_per_scoop == 1.50

def test_icecream_updated():
    ic = IceCream("Pistachio", 2, 1.50)
    ic.name = "Vanilla"
    ic.scoop_count = 3
    ic.price_per_scoop = 2.00
    assert ic.name == "Vanilla"
    assert ic.scoop_count == 3
    assert ic.price_per_scoop == 2.00

# Sundae Tests
def test_sundae_default():
    s = Sundae()
    assert s.name == ""
    assert s.scoop_count == 0
    assert s.price_per_scoop == 0.0
    assert s.topping_name == ""
    assert s.topping_price == 0.0

def test_sundae_provided():
    s = Sundae("Vanilla", 2, 1.50, "Hot Fudge", 0.99)
    assert s.name == "Vanilla"
    assert s.scoop_count == 2
    assert s.price_per_scoop == 1.50
    assert s.topping_name == "Hot Fudge"
    assert s.topping_price == 0.99

def test_sundae_updated():
    s = Sundae("Vanilla", 2, 1.50, "Hot Fudge", 0.99)
    s.name = "Chocolate"
    s.scoop_count = 3
    s.price_per_scoop = 2.00
    s.topping_name = "Caramel"
    s.topping_price = 1.25
    assert s.name == "Chocolate"
    assert s.scoop_count == 3
    assert s.price_per_scoop == 2.00
    assert s.topping_name == "Caramel"
    assert s.topping_price == 1.25