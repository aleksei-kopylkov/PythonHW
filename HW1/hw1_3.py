from random import randint

rand_num = randint(0, 1001)

for _ in range(10):
    guess_num = int(input("Введите число: "))
    if guess_num == rand_num:
        print("Вы угадали")
        break
    elif guess_num > rand_num:
        print("Введенное число больше загаданного")
    elif guess_num < rand_num:
        print("Введенное число меньше загаданного")

