#
#
# # items = []
# # names = list()
#
# # fruits = ["яблоко", "банан", "груша"]
# # print(fruits[0])
# # print(fruits[-1])
# #
# # fruits[1] = "апельсин"
# # print(fruits)
#
# # del fruits[0]
# # print(fruits)
#
# # items = [1, 2, 3, 4, 5, 6, 7, 8]
# # print(items[1:4])
# # print(items[2:])
# # print(items[:5])
# # print(items[1:5:2])
# # print(items[::-1])
# # items.reverse()
# # print(items)
#
# '''
# .append(x) - добавит элемент в конец списка
# .insert(i,x) -вставляет элемент x по индексу i,
# и сдвигает все остальные элементы вправо.
# .pop([i]) -удаляет i- элемент и возвращает его. если не указан i то удалится последний элемент.
# .remove() удаляет значение из списка - первое попавшееся
# .copy() - Копирует список (поверхностно)
# .clear() - очищает список полностью.
# .count(i) - проверяет сколько i находится в списке
# .extend(lst2) - расширяет список на те значения что указаны во втором списке
# .index(i) - узнать индекс значения
# '''
# from pythonProject.lesson3 import number
#
# fruits = ["яблоко", "банан", "груша"]
#
# # fruits.append("слива")
# # print(fruits)
# #
# # fruits.insert(0, "персик")
# # print(fruits)
# #
# fruits.insert(100, "мандарин")
# print(fruits)
# print(fruits.index("мандарин"))
#
# # last = fruits.pop(0)
# # print(fruits)
# # print(last)
#
# # last = fruits.remove("банан")
# # print(fruits)
# # print(last)
#
#
# # fruits = ["яблоко", "банан", "груша"]
# # fruits2 = ["апельсин", "мандарин", "ананас"]
# # fruits.extend(fruits2)
# # print(fruits)
#
# # numbers = [5, 2, 2, 2, 25, 33, 123]
# # # print(numbers.count(2))
# #
# # numbers.append("hello")
# # numbers.insert(0, ["a", "b", "c"])
# # print(numbers)
#
#
# # list() -создает список
# # sorted() -возвращает новый отсортированный список
# # len() - возвращает длинну списка
# # sum() возвращает сумму элементов /значения одинаковых типов
# # min() - возвращает минимальное значение списка /значения одинаковых типов
# # max()- возвращает максимальное значение списка /значения одинаковых типов
#
# # numbers = [4, 1, 9, 2]
# # # print(len(numbers))
# # # print(sum(numbers))
# # # print(min(numbers))
# # # print(max(numbers))
# # # print(sorted(numbers))
# #
# #
# # numbers.sort()
# # print(numbers)
# #
# # fruits = ["яблоко", "груша", "апельсин"]
# #
# # for fruit in fruits:
# #     print("Я люблю", fruit)
#
#
# # grades = [2, 5, 3, 4, 5, 2, 5]
# # excellent = []
# #
# # for grade in grades:
# #     if grade == 5:
# #         excellent.append(grade)
# #
# # print("Отличные оценки", excellent)
# # print(excellent.count(5))

# numbers = []
#
# for i in range(1, 11): # 1 2 3 4 5 6 7 8 9 10
#     numbers.append(i)
#
# print("Список чисел от 1 до 10:", numbers)
#
# even_numbers = []
#
# for i in range(1, 21): # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#     if i % 2 == 0:
#         even_numbers.append(i)
#
# print(even_numbers)

# fruits = ["яблоко", "банан", "груша"]
# print("банан" in fruits)
# print("слива" in fruits)

# matrix = [[1, 2], [3, 4], [5, 6]]
# print(matrix[0])
#
# print(matrix[2][0])



#
# num = []
# for i in range(1, 31):
#     num.append(i)
#
# print(num)
#
# num2 = [i for i in range(1, 31)]
# print(num2)
#
# num3 = [i + 1 for i in range(1, 31)]
# print(num3)

# num3 = []
# for i in range(1, 31):
#     if i % 2 == 0:
#         num3.append(i)
# print(num3)
#
# num4 = [i for i in range(1 ,31) if i % 2 ==0]
# print(num4)

















































