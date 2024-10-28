# Виртуальное окружение, модули, библиотеки, фреймворки

# 1 - вид встроенные\внутренний модули
# import random, time, sqlite3
import math
print(math.pi)

# вызов отдельных компонентов из модулей
from math import e, pi, sin, sqrt
print(e)


# 2 - вид собвственные модули
from lesson4_2 import Remanga
n = Remanga('огненный кулак')
n.manga_upp()


# внешние модули, для использования нужно скачать
from art import tprint
tprint('hello')

import colorama
