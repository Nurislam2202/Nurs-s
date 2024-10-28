# Инкапсуляция
# 1 публичный, 2 _защищенный,3 __скрытый

# супер класс\родительский класс
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def go(self):
        print(self.x, self.y)


a = A('x', 'y')


# дочерний класс
class B(A):
    def __str__(self):
        return f'x: {self.x} y: {self.y}'

    def go(self):
        print('метод класса B')
        super().go()


b = B('x', 'y')


# b.go()
# print(b)
# print(a)


class Bank:
    def __init__(self, name, pin, money):
        self.name = name
        self._pin = pin
        self.__money = money

    def __str__(self):
        return f'{self.name}: {self.__money}'

    def setpin(self, pin):
        self._pin = pin

    def getpin(self):
        print(self._pin)

    @property
    # getter
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    @money.deleter
    def money(self):
        del self.__money


client = Bank('Marlen', '2525', 10_000_000)

print(client)
client.setpin(12432)
client.getpin()
client._pin = 4444
client.getpin()

# client.setmoney(20000)
client._Bank__money = 0
print(client)
client.money = 10000
print(client.money)
del client.money
client.money = 1
print(client)
print(dir(client))
