
# username = "admin"
# username2 = "Admin"
#
# print(username == username2)
# print(username.lower() == username2.lower())
#
#
# temperature = 3
#
# if temperature < 5:
#     print("Очень холодно!")
# else:
#     print("Погода плюсовая, можно гулять без шапки!")


# age = 19
#
# if age <= 18:
#     print("Вход запрещен!")
#     print("Тебе нет 18!")

# else:
#     print("Вход разрешен!")

#
# temperature = 4
#
# if temperature < 5:
#     print("Очень холодно!")
#
# elif temperature <= 15:
#     print("Прохладно")
#
# elif temperature < 25:
#     print("Тепло")
#
# else:
#     print("Жарко")


# age = 15
#
# if age <= 7:
#     if gender == "Ж":
#         print("девочка")
#     else:
#         print("мальчик")
# elif age <= 18:
#     if gender == "Ж":
#         print("девушка")
#     else:
#         print("юноша")
#
# else:
#     print("взрослый")
#

#дополнительные условия	and , or , not

# gender = "М"
# age = 18
# passage = True
#
# if age >= 18 or passage:
#     print("Проход разрешен")
# else:
#     print("Проход запрещен")

# if age >= 18 and passage and gender == "Ж":
#     print("Проход разрешен!")
#
# else:
#     print("Проход запрещен")


# wifi_on = True
#
# if not wifi_on:
#     print("Нет подключения к интернету")
# else:
#     print("Интернет работает")


# if 1:
#     print("Hello")
# if 123:
#     print("Hello")
# if 0:
#     print("Hello")

# 1, 123, 2.3 == True
# 0, 0.0, "", [], , None == False
#
# #
# day = 30
#
# match day:
#     case 1:
#         print("понедельник")
#     case 2:
#         print("вторник")
#     case 3:
#         print("среда")
#     case 4:
#         print("четверг")
#     case 5:
#         print("пятница")
#     case 6:
#         print("суббота")
#     case 7:
#         print("воскресенье")
#     case _:
#         print("ошибка: проверьте значение")
#
# n = int(input("Введите число от 1 до 10: "))
#
# match n:
#     case 1 | 3 |5 |7 | 9 :
#         print("нечетное число")
#     case 2 | 4 | 6 | 8 | 10 :
#         print("четное число")
#     case _:
#         print("ошибка, проверьте число")


