# 查看.h5文件的内容

import h5py
import numpy as np

file = h5py.File("actor_0238_2154404724.h5", "r")
for data in file.keys():
	print(data)
	print(file[data])
	print(np.shape(file[data][0]))

# 文件中内容格式：{data: , label: }
# 其中data的shape是（1000，1，1）
# 其中label的shape是（21，1，1）
