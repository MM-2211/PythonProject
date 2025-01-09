data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

numbers = []
letters = []

for item in data_tuple:
    if isinstance(item, str) in data_tuple:
        letters.append(item)
    elif isinstance(item, bool) in data_tuple:
        letters.append(item)
    else:
        numbers.append(item)

numbers.remove(6.13)
numbers.insert(1, 2)
letters.remove(True)
letters.insert(8, True)
numbers.sort()
letters.reverse()
letters.remove("g")
letters.remove("C")
letters.insert(1, "G")
letters.insert(7, "c")

numbers = [item ** 2 for item in numbers]

numbers = tuple(numbers)
letters = tuple(letters)

print(letters)
print(numbers)
