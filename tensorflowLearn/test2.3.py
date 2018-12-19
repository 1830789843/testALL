# 在python console中可以查看实时的结果
import tensorflow as tf

a = tf.constant([1.0, 2.0], name="a")
b = tf.constant([2.0, 3.0], name="b")

# 结果是对应元素相加。
result = a + b

sess = tf.Session()
# 输出，即，array([3., 5.], dtype=float32)
sess.run(result)
