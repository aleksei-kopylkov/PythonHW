def convert_to_hex(num = int(input())):
    res = ""
    while num > 0:
        if num % 16 == 10:
            res = "a" + res
        elif num % 16 == 11:
            res = "b" + res
        elif num % 16 == 12:
            res = "c" + res
        elif num % 16 == 13:
            res = "d" + res
        elif num % 16 == 14:
            res = "e" + res
        elif num % 16 == 15:
            res = "f" + res
        else:
            res = str(num % 16) + res
        num //= 16
    return res

print(convert_to_hex())
print(hex(199))