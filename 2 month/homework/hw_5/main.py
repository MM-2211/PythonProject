from decouple import config
from logic import make_bet, is_game_over

def main():
    min_num = config("min_num", cast=int)
    max_num = config("max_num", cast=int)
    num_attempts = config("num_attempts", cast=int)
    start_money = config("start_money", cast=int)
    money = start_money

    print(f"Начальный баланс: {money}, Количество попыток: {num_attempts}")

    while not is_game_over(num_attempts, money):
        print(f"Введите вашу ставку и число от {min_num} до {max_num}: ")

        try:
            player_money, player_num = map(int, input().split())

            if player_money > money:
                print(f"У вас недостаточно деньги{player_money}!")
                continue

            if not (min_num <= player_num <= max_num):
                print(f"Число должно быть в диапазоне от {min_num} до {max_num}")
                continue
        except ValueError:
            print("Вводите ввиде целых чисел!")
            continue

        money, won = make_bet(player_money, player_num, money, min_num, max_num)

        num_attempts -= 1

        print(f"Текущий капитал: {money}, осталось попыток: {num_attempts}")
        if won:
            print("Поздравляю, вы выиграли ставку!")
        print("-----")

    print("Game over")

if __name__ == "__main__":
    main()




