num = int(input())
if num < 0 or num > 100000:
    print("Некорректное число")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Число не является простым.")
            break
    else:
        print(num, "- простое число.")