# # from functions import add, multiply

# from pythonProject.lesson3 import number
#
#
# # #
# # # print(fn.add(3, 5))
# # # print(fn.multiply(3, 5))
# # # print(fn.divide(15, 3))
# #
# # #
# # def greet(name):
# #     return f"Привет, {name}!"
# # #
# # # items = [1, "текст", fn.greet]
# # #
# # # print(items)
# # #
# # # print(items[2]("Аня"))
# #
# # def call_function(f, value):
# #     print("Результат работы функции:", f(value))
# #
# # call_function(fn.greet, "Иван")

# def is_positive(x):
#     return x > 0
#
# def is_negative(x):
#     return x < 0
#
# def filter_list(lst, func):
#     return [x for x in lst if func(x)]

# import functions as fn
# # from functions import add, multiply
#
# numbers = [-3, -1, 0, 5, 7, -10]
#
# print(fn.filter_list(numbers, fn.is_positive))
# print(fn.filter_list(numbers, fn.is_negative))
#
# print(fn.add(3, 5, 10, 10))


# def square(x):
#     return x ** 2


# square = lambda x: x ** 2
# print(square(5))

numbers = [-3, -1, 0, 5, 7, -10]

negative = list(filter(lambda x: x < 0, numbers))
print(negative)



