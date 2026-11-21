from abc import ABC, abstractmethod
from packaging import Packaging
from payment import PayType, Payable


class DessertItem(ABC, Packaging):
    def __init__(self, name: str = ""):
        self.name = name
        self.tax_percent = 7.25
        self.packaging = None

    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    def calculate_tax(self) -> float:
        return round(self.calculate_cost() * (self.tax_percent / 100), 2)


class Candy(DessertItem):
    def __init__(self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"

    def calculate_cost(self) -> float:
        return round(self.candy_weight * self.price_per_pound, 2)

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.packaging})\n"
            f"-    {self.candy_weight} lbs. @ ${self.price_per_pound:.2f}/lb:, "
            f"${self.calculate_cost():.2f}, [Tax: ${self.calculate_tax():.2f}]"
        )


class Cookie(DessertItem):
    def __init__(self, name: str = "", cookie_quantity: int = 0, price_per_dozen: float = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"

    def calculate_cost(self) -> float:
        return round((self.cookie_quantity / 12) * self.price_per_dozen, 2)

    def __str__(self) -> str:
        return (
            f"{self.name} Cookies ({self.packaging})\n"
            f"-    {self.cookie_quantity} cookies. @ ${self.price_per_dozen:.2f}/dozen:, "
            f"${self.calculate_cost():.2f}, [Tax: ${self.calculate_tax():.2f}]"
        )


class IceCream(DessertItem):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"

    def calculate_cost(self) -> float:
        return round(self.scoop_count * self.price_per_scoop, 2)

    def __str__(self) -> str:
        return (
            f"{self.name} Ice Cream ({self.packaging})\n"
            f"-    {self.scoop_count} scoops. @ ${self.price_per_scoop:.2f}/scoop:, "
            f"${self.calculate_cost():.2f}, [Tax: ${self.calculate_tax():.2f}]"
        )


class Sundae(IceCream):
    def __init__(
        self,
        name: str = "",
        scoop_count: int = 0,
        price_per_scoop: float = 0.0,
        topping_name: str = "",
        topping_price: float = 0.0,
    ):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"

    def calculate_cost(self) -> float:
        return round(super().calculate_cost() + self.topping_price, 2)

    def __str__(self) -> str:
        return (
            f"{self.topping_name} {self.name} Sundae ({self.packaging})\n"
            f"-    {self.scoop_count} scoops. @ ${self.price_per_scoop:.2f}/scoop\n"
            f"-    {self.topping_name} topping @ ${self.topping_price:.2f}:, "
            f"${self.calculate_cost():.2f}, [Tax: ${self.calculate_tax():.2f}]"
        )


class Order(Payable):
    def __init__(self):
        self.order = []
        self._index = 0
        self.pay_type: PayType = PayType.CASH

    def add(self, item: DessertItem):
        self.order.append(item)

    def get_pay_type(self) -> PayType:
        if not isinstance(self.pay_type, PayType):
            raise ValueError(f"Invalid payment type: {self.pay_type}")
        return self.pay_type

    def set_pay_type(self, payment_method: PayType) -> None:
        if not isinstance(payment_method, PayType):
            raise ValueError(f"Invalid payment method: {payment_method}")
        self.pay_type = payment_method

    def order_cost(self) -> float:
        return round(sum(item.calculate_cost() for item in self.order), 2)

    def order_tax(self) -> float:
        return round(sum(item.calculate_tax() for item in self.order), 2)

    def __len__(self):
        return len(self.order)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.order):
            item = self.order[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

    def __str__(self) -> str:
        lines = []
        lines.append("Name, Cost, Tax")
        for item in self.order:
            lines.append(str(item))
            lines.append("")

        lines.append("-------------------------------,----------,------------")
        lines.append(f"Total number of items in order:, {len(self.order)},")
        lines.append(f"Order Subtotals:, ${self.order_cost():.2f}, [Tax: ${self.order_tax():.2f}]")
        lines.append(f"Order Total:,, ${self.order_cost() + self.order_tax():.2f}")
        lines.append("-------------------------------,----------,------------")
        lines.append(f"Paid with {self.get_pay_type().name}")

        return "\n".join(lines)

    def to_list(self) -> list:
        lines = str(self).split("\n")
        data = []
        for line in lines:
            data.append(line.split(","))
        return data