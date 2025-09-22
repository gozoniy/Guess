from logic import secret_number, check_guess, MIN_NUMBER, MAX_NUMBER

def main():
    print(f"Добро пожаловать, Ваша игра взломана! Вы никогда не угадаете число.")
    s = secret_number()
    attempts = 0
    while True:
        raw = input("Ваш вариант: ")
        try:
            g = int(raw)
        except ValueError:
            print("Введите целое число.")
            continue
        attempts += 1
        res = check_guess(s, g)
        if res == "Верно":
            print(f"Вы угадали за {attempts} попыток!")
            break
        else:
            print(res)

if __name__ == "__main__":
    main()
