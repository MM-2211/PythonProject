# Функции: виды параметров, возвращение данных, виды аргументов
# DRY - don't repeat yourself
# def - define

"""" из чего состоит функция """
# определение наименование(параметры):
#     тело функции
#     возвращение объекта(результата)
#
# вызов функции
# наименование(аргументы)

# def some_function(name="известна", surname="неизвестна"): # required positional parametr
#     print(f"name: {name}, surname: {surname}")
#
# some_function("adilet", "tairov") # required posotoinal arguments
# some_function(surname="tyson", name="mike") #kewywords arguments
# some_function()

# square_2 = get_square(7, 5)
# square_victory = get_square(width=110, length=350)
# square_hall = get_square(
#     int(input("Enter length")),
#     int(input("Enter width")),
# )
#
# print(square_2, square_victory, square_hall, sep="\n")


# lenght = 7
# width = 5
# square_2 = lenght * lenght
# print(square_2)

# lenght = 320
# width = 150
# square_victory = lenght * lenght
# print(square_victory)


# def menu(**kwargs):
#     return kwargs
#
# monday = menu(eat="pizza", drink="cola", dfg=324, sfs=5)
# print(monday)
#
#
# def plus(*args):
#     return sum(args), args[0]
#
# print(plus(3, 5, 3, 5, 6, 7,))
# print(plus(3, 5, 3, 5, 6, 7, 45, 45, 34, 65))


# def get_square(length: int, width: int) -> int:
#     """  Принимает длинну и ширину, возвращает площадь """
#     square = length * width
#     return square

# print(help(get_square))
# print(get_square.__doc__)
# print(get_square.__annotations__)




