def gen_example():
    print("before any yield")
    yield "first yield"
    print("between yields")
    yield "second yield"
    print("no yield anymore")


gen = gen_example()
gen.__next__()
gen.__next__()
gen.__next__()
