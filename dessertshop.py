from dessert import Order, Candy, Cookie, IceCream, Sundae
from payment import PayType
from tabulate import tabulate


class DessertShop:
    def user_prompt_candy(self) -> Candy:
        name = input("Enter name of candy: ")

        while True:
            try:
                weight = float(input("Enter weight (lbs): "))
                if weight >= 0:
                    break
                print("Weight must be greater than or equal to 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            try:
                price = float(input("Enter price per pound: "))
                if price >= 0:
                    break
                print("Price must be greater than or equal to 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        return Candy(name, weight, price)

    def user_prompt_cookie(self) -> Cookie:
        name = input("Enter name of cookie: ")

        while True:
            try:
                quantity = int(input("Enter quantity purchased: "))
                if quantity >= 0:
                    break
                print("Quantity must be greater than or equal to 0.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            try:
                price = float(input("Enter price per dozen: "))
                if price >= 0:
                    break
                print("Price must be greater than or equal to 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        return Cookie(name, quantity, price)

    def user_prompt_icecream(self) -> IceCream:
        name = input("Enter the type of ice cream: ")

        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops >= 0:
                    break
                print("Number of scoops must be greater than or equal to 0.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            try:
                price = float(input("Enter the price per scoop: "))
                if price >= 0:
                    break
                print("Price must be greater than or equal to 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        return IceCream(name, scoops, price)

    def user_prompt_sundae(self) -> Sundae:
        name = input("Enter the type of ice cream: ")

        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops >= 0:
                    break
                print("Number of scoops must be greater than or equal to 0.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        while True:
            try:
                price = float(input("Enter the price per scoop: "))
                if price >= 0:
                    break
                print("Price must be greater than or equal to 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        topping_name = input("Enter the topping: ")

        while True:
            try:
                topping_price = float(input("Enter the price for the topping: "))
                if topping_price >= 0:
                    break
                print("Price must be greater than or equal to 0.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        return Sundae(name, scoops, price, topping_name, topping_price)

    def user_prompt_payment(self) -> PayType:
        payment_prompt = "\n".join([
            "1:CASH",
            "2:CARD",
            "3:PHONE",
            "Enter payment method): "
        ])

        while True:
            choice = input(payment_prompt).strip()
            match choice:
                case "1":
                    return PayType.CASH
                case "2":
                    return PayType.CARD
                case "3":
                    return PayType.PHONE
                case _:
                    print("Invalid payment method. Please enter 1, 2, or 3.")


def main():
    shop = DessertShop()
    order = Order()

    done: bool = False
    prompt = '\n'.join([
        '\n',
        '1: Candy',
        '2: Cookie',
        '3: Ice Cream',
        '4: Sundae',
        '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])

    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response:  Please enter a choice from the menu (1-4) or Enter')
    print()

    payment_method = shop.user_prompt_payment()
    order.set_pay_type(payment_method)
    print()

    print(tabulate(order.to_list(), tablefmt="fsql"))


if __name__ == "__main__":
    main()