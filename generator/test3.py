def gen_generator():
    yield 1


def gen_value():
    return 1


if __name__ == '__main__':
    ret = gen_generator()
    print(ret, type(ret))  # <generator object gen_generator at 0x02645648> <type 'generator'>
    ret = gen_value()
    print(ret, type(ret))  # 1 <type 'int'>
