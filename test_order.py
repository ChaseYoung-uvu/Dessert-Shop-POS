import pytest
from dessert import Order
from payment import PayType


def test_order_payment_cash():
    order = Order()
    assert order.get_pay_type() == PayType.CASH
    order.set_pay_type(PayType.CASH)
    assert order.get_pay_type() == PayType.CASH


def test_order_payment_card():
    order = Order()
    order.set_pay_type(PayType.CARD)
    assert order.get_pay_type() == PayType.CARD


def test_order_payment_phone():
    order = Order()
    order.set_pay_type(PayType.PHONE)
    assert order.get_pay_type() == PayType.PHONE


def test_order_set_invalid_payment_type():
    order = Order()
    with pytest.raises(ValueError):
        order.set_pay_type("BITCOIN")  # type: ignore[arg-type]


def test_order_get_invalid_payment_type():
    order = Order()
    order.pay_type = "INVALID"  # type: ignore[assignment]
    with pytest.raises(ValueError):
        order.get_pay_type()