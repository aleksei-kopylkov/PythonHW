from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001
AMOUNT_OF_GUESSES = 10

rand_num = randint(LOWER_LIMIT, UPPER_LIMIT)

for _ in range(AMOUNT_OF_GUESSES):
    guess_num = int(input("Введите число: "))
    if guess_num == rand_num:
        print("Вы угадали")
        break
    elif guess_num > rand_num:
        print("Введенное число больше загаданного")
    elif guess_num < rand_num:
        print("Введенное число меньше загаданного")

