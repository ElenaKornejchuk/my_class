# a = range(5) # 0 1 2 3 4
#
# print(a)
from itertools import count
from pprint import pprint
from tabnanny import check

# for <имя переменной> <итерируемый объект>

# for i in range(5): # 0 1 2 3 4
#     print("Hello")

# for i in range(5): # 0 1 2 3 4
#     print(i)

# for i in range(4, 10, 2): # 4 5 6 7 8 9
#     print(i)

# for i in 100:
#     print(i)

# for c in "Hello": # H e l l o
#     print(c)
#
# text = "Hello"
# for c in text:
#     print(c)
#
# for i in range(len(text)): # 0 1 2 3 4
#     print(i)

# for i in range(len(text)):  # H e l l o  # 0 1 2 3 4
#     if i % 2 == 0:
#         print(text[i])

# i, j, k - для числовых значение сгенерированных в range
# c - для строк
#
# for _ in range(5):
#     print("hello")
#
# for i in range(5):
#     print(i)
#
# login = "admi"
# flag = True
#
# for c in login:
#     if c in "!@# $%":
#         flag = False
#         continue
# if len(login) < 5:
#     flag = False
#
# if flag:
#     print("Логин корректный")
#
# else:
#     print("Логин не подходит")





































# n = 10
#
# while n > 0:
#     print(n)
#     n = n - 1

# while True:
#     s = input()
#     if s  == "x":
#         break

# Напишите программу, которая считает от 5 до 1
# и выводит числа на экран. После окончания
# счёта программа должна вывести сообщение "Старт!".

# count = 5
#
# while count > 0:
#     print(count)
#     count -= 1
#
# print("Старт")

# Сделайте программу, которая спрашивает у
# пользователя текст и повторяет его обратно.
# Программа должна работать, пока
# пользователь не введёт слово "стоп".

# text = ""
#
# while text != "стоп":
#     text = input("Введите что-нибудь или слово 'стоп' для выхода: ")
#     if text != "стоп":
#         print("Вы написали:", text)
#
# print("Программа завершена")


# num = int(input("Введите число: ")) # 4863
#
# min = 9
# max = 0
#
# while num > 0:            # 4863
#     check_i = num % 10    # 4.8
#     if check_i > max:
#         max = check_i     # 8
#     if check_i < min:
#         min = check_i     # 3
#     num //= 10            # 4
#
# print(f"Максимальная цифра {max}, минимальная цифра {min}")

# '''программа должна попросить
# пользователя ввести текст
# и потом спросить у него букву
# и посчитать сколько раз эта
# буква встречается
# '''
#
# text = input("Введите текст: ")
# letter = input("Введите букву для подсчета: ")
#
# count = 0
# for c in text: # hello world
#     if c == letter:
#         count += 1
#
# print(f"Буква '{letter}' встречается {count} раз")
#
#
# print("Отличные оценки:", excellent)
# print(excellent.count(5))