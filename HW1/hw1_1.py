a, b, c = int(input("Введите a: ")), int(input("Введите b: ")), int(input("Введите c: "))
if a == b == c:
    print("Треугольник равносторонний")
elif a == b != c or a == c != b or b == c != a:
    print("Треугольник равнобедренный")
elif a + b < c or a + c < b or b + c < a:
    print("Такого треугольника не существует")
else:
    print("Такой треугольник существует.")