# def guess_number():
#     low = 1
#     high = 100
#     attempts = 0
#     guesses = []
#
#     while True:
#         attempts += 1
#         guess = (low + high) // 2
#         guesses.append(guess)
#
#         print(f"Попытка #{attempts}: Я думаю, что это число {guess}.")
#         user_input = input("Я угадал или это число больше/меньше? (больше/меньше/да): ").lower()
#
#         if user_input not in ["больше", "меньше", "да"]:
#             print("Пожалуйста, вводите только 'больше', 'меньше' или 'да'.")
#             continue
#         if user_input == "да":
#             with open("results.txt", "w") as file:
#                 file.write(f"Число загадано за {attempts} попыток.\n")
#                 file.write("Список попыток: " + ", ".join(map(str, guesses)) + "\n")
#                 file.write(f"Загаданное число: {guess}\n")
#             print("Я угадал ваше число!")
#             break
#         elif user_input == "больше":
#             low = guess + 1
#         elif user_input == "меньше":
#             high = guess - 1
#
# if __name__ == "__main__":
#     guess_number()

