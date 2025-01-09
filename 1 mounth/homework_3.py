vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
consonants = "bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщъьBCDFGHJKLMNPQRSTVWXYZБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"

while True:
    word = input("Введите слово на русском или на английском: ")
    if word == "cтоп" or word == "stop":
        break

    vowels_num = 0
    consonants_num = 0

    for letter in word:
        if letter in vowels:
            vowels_num += 1
        elif letter in consonants:
            consonants_num += 1

    letters_num = vowels_num + consonants_num

    if letters_num > 0:
        vowels_per = 100 * (vowels_num / letters_num)
        consonants_per = 100 * (consonants_num / letters_num)


    vowels_per = round(vowels_per, 2)
    consonants_per = round(consonants_per, 2)

    print(f"Количество букв: {letters_num}")
    print(f"Согласных букв: {consonants_num}")
    print(f"Согласных букв: {vowels_num}")
    print(f"Процент гласных/согласных: {vowels_per}%/{consonants_per}%")



