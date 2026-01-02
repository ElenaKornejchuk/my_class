# def say_hello(name):
#     return f"Привет, {name}!"
# from collections import Counter
# from itertools import zip_longest
#
# result = say_hello("Ivan")
# print(result)
#
# def decor(func):
#     def wrapper():
#         print("Старт")
#         func()
#         print("Финиш")
#     return wrapper
#
# @decor
# def say_hello():
#      print(f"Привет!")
#
# decorated_function = decor(say_hello)
# decorated_function()
#
# say_hello()
#
# def decor_2(func):
#     def wrapper(*args, **kwargs):
#         print("Начало функции")
#         result = func(*args, **kwargs)
#         print("Конец функции")
#         return result
#     return wrapper
#
# @decor_2
# def greet(name):
#     print(f"Привет, {name}!")
#
# greet("Ivan")
#
#
# @decor_2
# def add(*args):
#     print(sum(args))
#
# add(1, 3, 4)
#
# import time
#
# from fastapi.dependencies.utils import request_body_to_args
#
#
# def timing_decor(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} выполнилась за {end - start:.5f} секунд")
#         return result
#     return wrapper
#
# @timing_decor
# def generate_numbers(n):
#     return[i**2 for i in range(n)]
#
# generate_numbers(100000)








