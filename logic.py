import random

MIN_NUMBER = 10
MAX_NUMBER = 1000

def secret_number():
    return random.randint(MIN_NUMBER, MAX_NUMBER)

def check_guess(secret: int, guess: int) -> str:
    if guess < secret:
        return "Маловато"
    elif guess > secret:
        return "Перебрали"
    else:
        return "Оооочень Верно"
