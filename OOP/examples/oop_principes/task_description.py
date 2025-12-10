"""ОПИСАНИЕ ЗАДАЧИ"""

# class Order:
#
#
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = 'open'
#
#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#
#     def total_price(self):
#         return sum(quantities * prices
#                    for quantities, prices in zip(self.quantities, self.prices)
#                    )
#
#     def pay(self, payment_type, security_code):
#         if payment_type == 'debit':
#             print('Обработка дебетового типа платежа')
#             print(f'Проверка кода безопасности: {security_code}')
#             self.status = 'paid'
#         elif payment_type == 'credit':
#             print('Обработка кредитного типа платежа')
#             print(f'Проверка кода безопасности: {security_code}')
#             self.status = 'paid'
#         else:
#             raise Exception(f'Неизвестный способ оплаты: {payment_type}')
#
#
# # Создаем заказ
# order = Order()
# # Добавляем товары в заказ
# order.add_item('Клавиатура', 1, 2500)
# order.add_item("SSD", 1, 7500)
# order.add_item("USB-кабель", 2, 250)
# # Печатаем стоимость заказа
# print(order.total_price())
# # Оплачиваем заказ
# order.pay('debit', '0372846')

# ----------------------------------------------------------------------------

"""ПРИНЦИП ЕДИНОЙ ОТВЕТСТВЕННОСТИ"""

# class Order:
#
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = 'open'
#
#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#
#     def total_price(self):
#         return sum(quantities * prices
#                    for quantities, prices in zip(self.quantities, self.prices)
#                    )
#
# class PaymentProcessor:
#
#     def pay_debit(self, order, security_code):
#         print('Обработка дебетового типа платежа')
#         print(f'Проверка кода безопасности: {security_code}')
#         order.status = 'paid'
#
#     def pay_credit(self, order, security_code):
#         print('Обработка кредитного типа платежа')
#         print(f'Проверка кода безопасности: {security_code}')
#         order.status = 'paid'
#
# order = Order()
# order.add_item("Клавиатура", 1, 2500)
# order.add_item("SSD", 1, 7500)
# order.add_item("USB-кабель", 2, 250)
#
# print(order.total_price())
# processor = PaymentProcessor()
# processor.pay_debit(order, "0372846")
# processor.pay_credit(order, "7383903")

# ----------------------------------------------------------------------------

"""ПРИНЦИП ОТКРЫТОСТИ/ЗАКРЫТОСТИ"""

# from abc import ABC, abstractmethod
#
# class Order:
#
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = 'open'
#
#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#
#     def total_price(self):
#         return sum(quantities * prices
#                    for quantities, prices in zip(self.quantities, self.prices)
#                    )
#
# class PaymentProcessor(ABC):
#
#     @abstractmethod
#     def pay(self, order, security_code):
#         pass
#
# class DebitPaymentProcessor(PaymentProcessor):
#     def pay(self, order, security_code):
#         print("Обработка дебетового типа платежа")
#         print(f"Проверка кода безопасности: {security_code}")
#         order.status = "paid"
#
# class CreditPaymentProcessor(PaymentProcessor):
#     def pay(self, order, security_code):
#         print("Обработка кредитного типа платежа")
#         print(f"Проверка кода безопасности: {security_code}")
#         order.status = "paid"
#
# order = Order()
# order.add_item("Клавиатура", 1, 2500)
# order.add_item("SSD", 1, 7500)
# order.add_item("USB-кабель", 2, 250)
# print(order.total_price())
# processor = DebitPaymentProcessor()
# processor.pay(order, "0372846")

# ----------------------------------------------------------------------------

"""ПРИНЦИП ПОДСТАНОВКИ БАРБАРЫ ЛИСКОВ"""

# from abc import ABC, abstractmethod
#
# class Order:
#
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = 'open'
#
#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#
#     def total_price(self):
#         return sum(quantities * prices
#                    for quantities, prices in zip(self.quantities, self.prices)
#                    )
#
# class PaymentProcessor(ABC):
#
#     @abstractmethod
#     def pay(self, order):
#         pass
#
# class DebitPaymentProcessor(PaymentProcessor):
#
#     def __init__(self, security_code):
#         self.security_code = security_code
#
#     def pay(self, order):
#         print("Обработка дебетового типа платежа")
#         print(f"Проверка кода безопасности: {self.security_code}")
#         order.status = "paid"
#
# class CreditPaymentProcessor(PaymentProcessor):
#
#     def __init__(self, security_code):
#         self.security_code = security_code
#
#     def pay(self, order):
#         print("Обработка кредитного типа платежа")
#         print(f"Проверка кода безопасности: {self.security_code}")
#         order.status = "paid"
#
# class PaypalPaymentProcessor(PaymentProcessor):
#
#     def __init__(self, email_address):
#         self.email_address = email_address
#
#     def pay(self, order):
#         print("Обработка Paypal платежа")
#         print(f"Использование адреса электронной почты: {self.email_address}")
#         order.status = "paid"
#
# order = Order()
# order.add_item("Клавиатура", 1, 2500)
# order.add_item("SSD", 1, 7500)
# order.add_item("USB-кабель", 2, 250)
# print(order.total_price())
# processor = PaypalPaymentProcessor("hi@company.com")
# processor.pay(order)

# ----------------------------------------------------------------------------

"""ПРИНЦИП РАЗДЕЛЕНИЯ ИНТЕРФЕЙСОВ"""

# from abc import ABC, abstractmethod
#
# class Order:
#
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = 'open'
#
#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#
#     def total_price(self):
#         return sum(quantities * prices
#                    for quantities, prices in zip(self.quantities, self.prices)
#                    )
#
# class PaymentProcessor(ABC):
#
#     @abstractmethod
#     def pay(self, order):
#         pass
#
# class PaymentProcessorSMS(PaymentProcessor):
#
#     @abstractmethod
#     def pay(self, order):
#         pass
#
#     @abstractmethod
#     def auth_sms(self, code):
#         pass
#
# class DebitPaymentProcessor(PaymentProcessorSMS):
#
#     def __init__(self, security_code):
#         self.security_code = security_code
#         self.verified = False
#
#     def auth_sms(self, code):
#         print(f'Верификация SMS кода {code}')
#         self.verified = True
#
#     def pay(self, order):
#         if not self.verified:
#             raise Exception('Не авторизован')
#         print("Обработка дебетового типа платежа")
#         print(f"Проверка кода безопасности: {self.security_code}")
#         order.status = "paid"
#
# class CreditPaymentProcessor(PaymentProcessorSMS):
#
#     def __init__(self, security_code):
#         self.security_code = security_code
#
#     def pay(self, order):
#         print("Обработка кредитного типа платежа")
#         print(f"Проверка кода безопасности: {self.security_code}")
#         order.status = "paid"
#
# class PaypalPaymentProcessor(PaymentProcessorSMS):
#
#     def __init__(self, email_address):
#         self.email_address = email_address
#         self.verified = False
#
#     def auth_sms(self, code):
#         print(f'Верификация SMS кода {code}')
#         self.verified = True
#
#     def pay(self, order):
#         if not self.verified:
#             raise Exception('Не авторизован')
#         print("Обработка paypal платежа")
#         print(f"Использование адреса электронной почты: {self.email_address}")
#         order.status = "paid"
#
# order = Order()
# order.add_item("Клавиатура", 1, 2500)
# order.add_item("SSD", 1, 7500)
# order.add_item("USB-кабель", 2, 250)
# print(order.total_price())
# processor = PaypalPaymentProcessor("hi@company.com")
# processor.auth_sms(465839)
# processor.pay(order)

# ----------------------------------------------------------------------------

"""
ПРИНЦИП ИНВЕРСИИ ЗАВИСИМОСТЕЙ

Принцип инверсии зависимостей (Dependency Inversion) — сделать классы
зависимыми от абстрактных классов, а не от обычных классов.
"""

from  abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        return sum(quantities * prices
                   for quantities, prices in zip(self.quantities, self.prices)
                   )


class Authorizer(ABC):

    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class AuthorizerSMS(Authorizer):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f'Верификация SMS кода {code}')
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class AuthorizerRobot(Authorizer):

    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception('Не авторизован')
        print('Обработка дебетового типа платежа')
        print(f'Проверка кода безопасности: {self.security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print('Обработка кредитного типа платежа')
        print(f'Проверка кода безопасности: {self.security_code}')
        order.status = 'paid'


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception('Не авторизован')
        print('Обработка paypal платежа')
        print(f'Использование адреса электронной почты: {self.email_address}')
        order.status = 'paid'


order = Order()
order.add_item("Клавиатура", 1, 2500)
order.add_item("SSD", 1, 7500)
order.add_item("USB-кабель", 2, 250)
print(order.total_price())

authorizer = AuthorizerRobot()
# authorizer = AuthorizerSMS()

authorizer.not_a_robot()
# authorizer.verify_code(465839)

processor = PaypalPaymentProcessor("hi@company.com", authorizer)
processor.pay(order)
