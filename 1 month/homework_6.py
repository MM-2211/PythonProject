
#1
# def password1():
#     user_pass = input("Введите пароль: ").upper().lower()
#     password_user = 0
#     for letter in user_pass:
#         password_user += 1
#     if password_user > 6 and user_pass.isalnum():
#         print(True)
#     else:
#         print(False)
#
# password1()


#2
# def f_num(seq1, num1 = 0):
#     close = seq1[0]
#     for i in seq1:
#         if abs(i - num1) < abs(close - num1):
#             close = i
#
#     return close
#
# print(f_num([3, 34, 7, 67, 24, 16.5, 23.7], 22.2))


# Это задание из прошлого урока, найти минимальное значение
# numbers = [41, 52, 38, 10, 50]
#
# def len1():
#     min_value = numbers[0]
#     for num in numbers:
#         if num < min_value:
#             min_value = num
#     return min_value
#
# print(len1())
