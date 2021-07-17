class Currency:
    counter = 0

    def __init__(self, amount):
        self.amount = amount
        self.__class__.counter += 1

    @staticmethod
    def exchange_rate(currency):
        return 4 * currency

    @classmethod
    def get_fields(cls):
        return cls.__name__


def exchange_rate(currency):
    return 4 * currency


euro = Currency(200)
dollar = Currency(200)
x = euro.exchange_rate(3)
y = Currency.exchange_rate(3)
z = exchange_rate(3)
print(x)
print(y)
print(z)
q = euro.get_fields()
w = Currency.get_fields()
print(q)
print(w)

print(Currency.counter)
print(euro.counter)
print(dollar.counter)
Currency.counter = 666
print(euro.counter)
print(dollar.counter)
