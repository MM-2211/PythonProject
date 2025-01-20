monday = float(input("Укажите расход за понедельник: "))
tuesday = float(input("Укажите расход за вторник: "))
wednesday = float(input("Укажите расход за среду: "))
thursday = float(input("Укажите расход за четверг: "))
friday = float(input("Укажите расход за пятницу: "))
saturday = float(input("Укажите расход за субботу: "))
sunday = float(input("Укажите расход за воскресенье: "))

summ = monday + tuesday + wednesday + thursday + friday + saturday + sunday
average_con = summ / 7
average_con = round(average_con, 1)

print(f'Сумма ваших расходов:{monday + tuesday + wednesday + thursday + friday + saturday + sunday} '
      f'и средний ваш расход в день:{average_con}')

# days = ("Понедельник", "Вторник", "Среду", "Четверг", "Пятницу", "Субботу", "Воскресенье",)
# summ = 0
# for day in days:
#       just = float(input(f"Введите ваши расходы за {day}: "))
#       summ += just
# average_con = summ / len(days)
# print(f'Сумма ваших расходов:{summ} 'f'и средний ваш расход в день:{average_con}')

# while True:
#       word = input("Укажите цвет светофора: ").upper().lower()
#       if word == "выход" or word == "Выход" or word == "ВЫХОД":
#             break
#       elif word == "красный":
#             print("Стой!")
#       elif word == "зеленый":
#             print("Иди!")
#       elif word == "желтый":
#             print("Готовься!")
#       else:
#             print("Неверно указан цвет")



