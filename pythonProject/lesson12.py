# def greet():
#     print("**************")
#     print("Привет, мир!")
#     print("**************")
#
# greet()
# greet()
# greet()
# from pythonProject.lesson3 import result
#
#
# print("**************")
# print("Привет, мир!")
# print("**************")
# print("**************")
# print("Привет, мир!")
# print("**************")
# print("**************")
# print("Привет, мир!")
# print("**************")
#
# def greet(name):
#     print(f"Привет, {name}")
#
# greet("Аня")
# greet("Иван")

# def add(a, b):
#     print(a + b)
#
# # add(2, 3)
# # add(10, 5)
# #
# # add(b=5, a=1)
#
# # add(2)
# add(b=5)
#
# return
#
# def add(a, b):
#     return(a + b)
#
# result = add(5, 6)
# print(result)

# def greet(name="Гость"):
#     print(f"Привет, {name}!")
#
# greet("Аня")
# greet()

#
# def calc_discount(price, discount=10):
#     '''
#     Вычисляет сумму товаров с учетом скидки
#     :price: Изначальная стоимость товара
#     :discount: Размер скидки, по умолчанию скидка = 10%
#     :return: Возвращает новую стоимость с учетом скидки
#     '''
#     new_price = price - (price * discount / 100)
#     print(new_price)
#     return new_price
#
# calc_discount(1000)
# calc_discount(1000, 20)


# def add(a, b, c, d):
#     return a + b + c + d
#
# def add_all(*args):
#     print(args)
#
# add_all(1, 2, 3, 4, 5)
from itertools import count

from pyexpat.errors import messages


# def add_all(*args):
#     return sum(args)
#
# result = add_all(1, 2, 3, 4, 5, 5)
# print(result)
#
# def show_info(**kwargs):
#     print(kwargs)

#
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# show_info(name="Anna", age=25, country="France")

# def demo(a, b, *args, **kwargs):
#     print("a:", a)
#     print("b", b)
#     print("args:", args)
#     print("kwargs:", kwargs)
#
# demo(1, 2, 3, 4, 5, x=6, y=7)
#
# def greet_all(*names):
#     for name in names:
#         print(f"Привет, {name}!")
#
# greet_all("Anna", "Max", "Ivan", "Maria")


# def greet_person(**info):
#     print(f"Привет, {info.get('name', 'гость')}")
#     print(f"Твоя страна, {info.get('country', 'не указана')}")
#
# greet_person(age=25, country="France")


# def say_hello1():
#     name = "Anna"
#     print("Привет,", name)
#
# def say_hello2():
#     name = "Maria"
#     print("Привет,", name)
#
# def say_hello3():
#     name = "Sofia"
#     print("Привет,", name)
#
# say_hello1()
# say_hello2()
# say_hello3()

#
# name = "Maria"
#
# def say_hello():
#     print("Привет,", name)
#
# say_hello()
#
# def say_hello2():
#     print("Как дела,", name)
#
# say_hello2()

#
# count = 0
#
# def increment(count):
#     # global count
#     count += 1
#     print("Счетчик:", count)
#
# increment(5)
# # increment()
# # increment()
# print(count)

# name = "Мир"
#
# def greet():
#     print("Привет,", name)
#
# greet()
# print(name)

# text = "Привет из внешней функции"
#
# def outer():
#     # text = "Привет из внешней функции"
#
#     def inner():
#         print(text)
#
#     inner()
#
# outer()

# def outer():
#     def inner():
#         message = "Привет из внутренней функции"
#         print(message)
#
#     inner()
#     print(message)
#
# outer()


# name = "Мир"
#
# def outer():
#     name = "Аня"
#
#     def inner():
#         name = "Катя"
#         print("Внутри inner:", name)
#
#     inner()
#     print("Внутри outer:", name)
#
# outer()
# print("Глобально:", name)

#
# def outer():
#     count = 0
#
#     def inner(count):
#         # nonlocal count
#         count += 1
#         print("Счетчик:", count)
#
#     inner(3)
#     print(count)
#
# outer()


