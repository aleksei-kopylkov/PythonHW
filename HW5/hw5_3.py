def fibbonaci(n):
    start_list = [1, 2]
    for i in range(n):
        start_list.append(start_list[-1] + start_list[-2])
        yield start_list[-1]


n = 4
fib = fibbonaci(n)
print(next(fib))
print(next(fib))

