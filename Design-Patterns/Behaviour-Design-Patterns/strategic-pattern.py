import types
import typing
import abc


class Strategy:

    def __init__(self, name='Strategy Example 0', func=None):
        self.name = name
        if func:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print (self.name)


def execute_replacement1(self):
    print(self.name + 'from execute 1')


def execute_replacement2(self):
    print(self.name + 'from execute 2')


def execute_replacement3(self):
    print(self.name + 'from execute 3')


st0 = Strategy()
strat1 = Strategy("Strategy Example 1", execute_replacement1)

strat2 = Strategy("Strategy Example 2", execute_replacement2)

strat3 = Strategy("Strategy Example 3")
strat3.execute = execute_replacement3 ## Monkey Patching

st0.execute()
strat1.execute()
strat2.execute()
strat3.execute(strat3)


class PaymentMode(abc.ABC):

    @abc.abstractmethod
    def pay(self, *args, **kwargs):
        pass


class CardPayment(PaymentMode):

    def pay(self, amount: float, **kwargs):
        print ("Payment Made by card")


class CashPayment(PaymentMode):
    def pay(self, amount, **kwargs):
        print ("Payment made by cash")


class Payment:

    def __init__(self, payment: PaymentMode):
        self._payment = payment

    @property
    def payment(self) -> PaymentMode:
        return self._payment

    @payment.setter
    def payment(self, payment: PaymentMode) -> None:
        self._payment = payment

    def make_payment(self, amount: float, **kwargs):
        self._payment.pay(amount, **kwargs)


_amount = 100

cash_payment = Payment(CashPayment())
cash_payment.make_payment(_amount)


card_payment = Payment(CardPayment())
card_payment.make_payment(_amount)
