# Список - list, кортежи. Индексы и срезы. Встроенные функции к наборам элементов. Списковое включение List comprehension

# objects = (True, 5.3, 7, "geeks")
# print(objects)
# print(type(objects))
#
# numbers = (45,)
# print(numbers)
# print(type(numbers))

""" Встроенные функции к наборам элементов"""
# numbers = [1, 2, 3, 4, 5]
# numbers = tuple(numbers)
# numbers = list(numbers)
# print(numbers)
# new = numbers.copy()
# new[0] = 6
# print(numbers)
# print(new)

# print(numbers == new)
# print(id(numbers))
# print(id(new))
# print(numbers is new)

# print(numbers)
# new_numbers = [number + 5 for number in numbers if number >= 3]
# print(new_numbers)

# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(any(numbers))
# print(all(numbers))
# print(isinstance(numbers, list))

# students = ["ramzan", "artur", "kairat", "ulukbek" ]
"""add"""
# students.append("zhanat")
# students.insert(3, "zhanat")
# students.extend(["aziim", "aisha", "miguel"])
# students += ["amir", "kylymbek"]
"""edit"""
# students[:2] = ["aisha"]
# students[:1] = ["amir", "azim", 'azim']
# students.reverse()
# students.sort(reverse=True)
# students[2] = "miguel"
# students[:2] = ["marlis", "amir"]
"""delete"""
# students.remove("ulukbek")
# deleted = students.pop(0)
# print(deleted)
# del students[1]
# del students[-2:]
# print(students)


""" Индексы и срезы [start:stop:step] """
# print(students[::-1])
# print(students[::2])
# print(students[:2])
# print(students[-2:])
# print(list(range(1, 6)))
# print(students[1:3])
# print(students[1:3:1])
# print(students[1:3])
# print(students[2:4:1])
# print(students[2:1])

# print(range(1, 6)[0])
# print("python"[2])
# print(students[0])
# print(students[2])
# print(students[-1])
# print(students[3])
#
# print(type(students))