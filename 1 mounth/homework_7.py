# # №1
# def nearest_num(numbers, target):
#     sorted_num = sorted(numbers, key=lambda x: abs(x - target))
#     return target, tuple(sorted_num)
# numbers = [234, 4563, 34, 145, 4432]
# target = 222
# result = nearest_num(numbers, target)
#
# print(result)
#
# # №2
# words = ["Пари Сен-Жермен", "Реал Мадрид", "Тоттенхэм", "Милан", "Боруссия"]
# long_words = list(filter(lambda word: len(word) > 8, words))
# print(long_words)
# numbers = [17, 22, 19, 5, 23]
# doubled_num = list(map(lambda x: x + 2000, numbers))
#
# print(doubled_num)
#
# # №3
# def element_index(iter=None):
#     if iter is None:
#         iter = [1, 2, 3, 4, 5]
#     while True:
#         user_input = input(f"Введите индекс от 0 до {len(iter) - 1}: ")
#         if user_input.lower() == 'стоп':
#             print("Программа завершена!")
#             break
#         try:
#             index = int(user_input)
#             print(f"Элемент по индексу {index}: {iter[index]}")
#         except IndexError:
#             print(f"Индекс неверный! Пожалуйста, введите индекс от 0 до {len(iter) - 1}.")
#         except ValueError:
#             print("Введите целое число!")
#
# print(element_index())

# Задание из класса
# data = {}
# ids = [22, 11, 5]
#
# for id in ids:
#     name = input(f"number {id}: ")
#     rates = None
#     while rates is None:
#         try:
#             rates = int(input(f"{name} please, enter rate: "))
#         except ValueError:
#             print("error detected")
#
#     data[name] = rates
#     print(data)
#
# print(sum(data.values()) / len(data))