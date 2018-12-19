RANGE_NUM = 100
for i in [x*x for x in range(RANGE_NUM)]:  # 第一种方法：对列表进行迭代
    # do sth for example
    print(i)

for i in (x*x for x in range(RANGE_NUM)):  # 第二种方法：对generator进行迭代
    # do sth for example
    print(i)

# 区别在于括号。前者为列表，后者为生成器
