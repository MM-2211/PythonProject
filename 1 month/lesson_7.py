# Lambda функции. Обработка исключений.

# lambda1 = lambda n1, n2: n1 + n2
# print(lambda1(2, 3))
#
# def def1(n1, n2):
#     return n1 + n2
# print(def1(2, 3))

# def up_first_letter(word: str) -> str:
#     return word.title()
#
# def show_words(func, objects):
#     for i in objects:
#         print(func(i))

# show_words(lambda word: word.title(), ["kemin", "taldy-bylak", "osh"])

# words = ["tokmok", "karakol", "kant"]
# show_words(up_first_letter, words)

# sorted(), filter(), map()

# cities = ["bishkek", "jalal-abad", "nookat", "cholpon-ata", "kemin"]
# sorted_cities = sorted(cities, key=lambda word: word[-1])
# filter_cities = list(filter(lambda word: "-" not in word, cities))
# map_cities = tuple(map(lambda word: word.upper(), cities))

# print(sorted_cities, filter_cities, map_cities, sep="\n")
# cities = [i.upper() for i in cities if "-" not in i]
# print(cities)

# try:
#     print(2 + "kg")
# except:
#     print("Ошибка найдена!")
# else:
#     print("Проверка прошла успешно!")
# finally:
#     print("Проверка завершена")
# print(float("python"))
def calculator(num1: float, operator: str, num2: float) -> float:
    try:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Оба числа должны быть типа int или float.")
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Ошбика! На ноль делить нельзя!")
            return num1 / num2
        elif operator == '**':
            return num1 ** num2
        elif operator == '%':
            return num1 % num2
        else:
            raise ValueError("Неверный оператор! Можно: +, -, *, /, **, %.")
    except (ValueError, ZeroDivisionError, TypeError) as e:
        return str(e)

print(calculator(22, '/', 0))
