from random import randint

def random_number(min_num, max_num):
    return randint(min_num, max_num)

def make_bet(player_money, player_num, money, min_num, max_num):
    random_num = random_number(min_num, max_num)

    if money < player_money:
        print("Извините, у вас недостаточно средств для ставки")
        return money, False

    if player_num == random_num:
        print("Поздравляю, вы угадали число! Ваша ставка удваивается!")
        money += player_money * 2
        return money, True
    else:
        print("Вы не угадали число. Ставка проиграна.")
        money -= player_money
        return money, False

def is_game_over(num_attempts, money):
    if num_attempts <= 0:
        print("Извините, у вас закончились попытки.")
    elif money <= 0:
        print("Извините, у вас закончились деньги.")
    return num_attempts <= 0 or money <= 0

