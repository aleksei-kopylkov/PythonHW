current_balance = 0
actions_counter = 0


def main():
    command = input("Какое действие хотите выполнить? (Пополнить/Снять/Выйти): ").lower()
    control(command)


def control(command):
    if command == 'пополнить':
        print(pop_up())
        over()
    elif command == 'снять':
        print(withdraw())
        over()
    elif command == 'выйти':
        print("До свидания")
    else:
        print("Неизвестная команда! Попробуйте еще", end="\n")
        main()



def pop_up():
    global current_balance
    if current_balance > 5_000_000:
        current_balance -= current_balance * 0.1
    amount = int(input("Внесите сумму кратную 50: "))
    if amount % 50 == 0:
        global actions_counter
        current_balance += amount
        actions_counter += 1
        if actions_counter > 3:
            current_balance += current_balance * 0.03
        return current_balance
    else:
        return "Некорректная сумма"


def withdraw():
    global current_balance
    if current_balance > 5_000_000:
        current_balance -= current_balance * 0.1
    amount = int(input("Укажите сумму снятия, кратную 50: "))
    fee = amount * 0.015
    if fee < 30:
        fee = 30
    elif fee > 600:
        fee = 600
    if amount % 50 == 0:
        global actions_counter
        if current_balance - amount - fee >= 0:
            current_balance -= amount
            actions_counter += 1
            return current_balance
        else:
            return "Недостаточно средств"
    else:
        return "Некорректная сумма"


def over():
    cont = input("Хотите продолжить? Введите 'да'/ 'нет': ")
    if cont == "да":
        main()
    else:
        return "До свидания"


main()