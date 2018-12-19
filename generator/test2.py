def generator_example():
    yield 1
    yield 2


if __name__ == '__main__':
    for e in generator_example():
        print(e)
        # output 1 2
