# user1 = {}
# user2 = dict()
# user3 = dict(name="Ivan")
#
# print(user3)
#
# user1 = {"name": "Ivan", "age": 35, "user": True}
#
# user2 = {
#     "name": "Ivan",
#     "age": 35,
#     "user": True
# }
#
# print(user1)
# print(user2)

# user = {
#     "name": "Ivan",
#     "age": 35,
#     "user": True
# }
#
# # print(user["age"])
#
# user["email"] = "ivanov@mail"
#
# user["name"] = "Sergey"
#
# del user["user"]
# print(user)

# info = [
#     {
#         "name": "Anna",
#         "age": 35,
#         "user": True
#     },
#     {
#         "name": "Max",
#         "age": 25,
#         "user": True
#     },
#     {
#         "name": "Fiona",
#         "age": 47,
#         "user": False
#     }
# ]

# print(info[1]["user"])

# info = [
# {"name": "Anna", "age": 35, "user": True},
# {"name": "Max", "age": 25, "user": True},
# {"name": "Fiona", "age": 47, "user": False, "bio": {'ж': True, "м": False}},
# ]
#
# print(info[2]["bio"]["м"])

'''
.get() позволяет безопасно получить значение по ключу
.setdefault() возвращает значение и, если ключа не было, создаёт его
.keys(),
.values() и
.items() позволяют удобно работать с ключами и значениями
'''


# user = {"name": "Ivan", "age": 28}

# print(user.get("surname", "Фамилия не указана"))
# print(user)
# print(user.setdefault("surname", "Не указана"))
# print(user)

# print(user.keys())
# print(user.values())
# print(user.items())
#
# '''
# .clear() очищает словарь
# .copy() создает поверхностную копию
# .pop() - удаляет из словаря ключ-значение
# по указанному ключу и возвращает его значение.'''
#
# user = {"name": "Ivan", "age": 28}
#
# user2 = user.copy()
# user.clear()
#
# print(user)
# print(user2)
#
#
# info = {"name": "Anna", "age": 35, "user": True}
#
# for key in info.keys():
#     print(key)
#
# for val in info.values():
#     print(val)
#
# for key, val in info.items():
#     print(key, val)

# users  = [
# {"name": "Ivan", "age": 28},
# {"name": "Anna", "age": 22},
# {"name": "Petr", "age": 35},
# 	]
#
# new_users = []
#
# for user in users:
#     if user["age"] < 30:
#         new_users.append(user)
#
# print(new_users)
#
# new_users2 = [user for user in users if user["age"] < 30]
# print(new_users2)

# text = "Hello World"
# letters = {}
#
# for char in text.lower():
#     if char.isalpha():
#         letters[char] = letters.get(char, 0) + 1
#
# print(letters)
#
# info = [
#     {"name": "Anna", "age": 35, "user": True},
#     {"name": "Anna2", "age": 25, "user": False},
#     {"name": "Anna3", "age": 47, "user": False},
# ]
#
# user_block = []
#
# for user in info:
#     if user["user"] == False:
#         user_block.append(user)
#
# print(user_block)
#
#
# keys = ["name", "age", "phone"]
# values = ["Maria", 25, "+71234567890"]
#
# info = dict(zip(keys, values))
# print(info)
#
# info2 = {}
# for i in range(len(keys)):
#     info2[keys[i]] = values[i]
#
# print(info2)

