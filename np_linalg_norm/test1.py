# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(9) - 4
print(a)
b = a.reshape((3, 3))
print(b)

# 向量的2范数。即绝对值平方求和再开根号
result1 = np.linalg.norm(a)
print(result1)

# 矩阵的Frobenius norm。同上
result2 = np.linalg.norm(b)
print(result2)

# 同上。向量是没有这个的
result3 = np.linalg.norm(b, 'fro')
print(result3)

# 向量。元素绝对值的最大值
result4 = np.linalg.norm(a, np.inf)
print(result4)

result5 = np.linalg.norm(b, np.inf)
print(result5)

result6 = np.linalg.norm(a, -np.inf)
print(result6)

result7 = np.linalg.norm(b, -np.inf)
print(result7)
