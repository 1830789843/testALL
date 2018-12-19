def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b


result = fib()
for i in range(10):
    print(result.__next__())
