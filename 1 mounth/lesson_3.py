# Операторы: принадлежности, назначения. Циклы.

"""Оператор принадлежности"""
# print("p" in "geeks")
# print("p" in "python")
# print(2 in range(1, 11))
# print(42 in range(1, 11))

"""Операторы назначения"""
# number = 5
# # number = number + 3
# number += 3 # 8
# number -= 1 # 7
# number *= 2 # 14
# number //= 2 # 7
# number **= 2 # 49
# number %= 2 # 1
# number /= 2 # 0.5
# print(number)

"""Цикл while"""

# rounds = 0
#
# while rounds < 100:
#     rounds += 1
#     if rounds == 50:
#         print("stop")
#         break
#     if rounds % 2 == 0:
#         continue
#     print("hello, world", rounds)


# counter = 10
# while counter > 0:
#     print(f"Осталось попыток: {counter}")
#     counter -= 1
#     time = input("Укажите время суток: ").lower()
#     if time == "stop":
#         break
#
#     if time == "morning" or time == "утро":
#         print("Good morning!")
#     elif time == "day" or time == "день":
#         print("Good afternoon!")
#     elif time == "evening" or time == "вечер":
#         print("Good evening!")
#     else:
#         print("hello! (Время суток нераспознано)")


"""Цикл for"""

# word = "KYRGYZSTAN"
# # iterable, index, item
# for letter in word:
#     if letter == "S":
#         break
#     if letter in "YRZ":
#         continue
#     print(letter)

# rates = 0
# students = 14
# for student in range(1, students+1):
#     answer = int(input(f"Введите сумму ваших оценок студент номер #{student}: "))
#     rates += answer
#     print(rates)
#
# print(rates / students)