# 计算图的使用
import tensorflow as tf

# 1.使用默认的计算图
a = tf.constant([1.0, 2.0], name="a")
print(a.graph is tf.get_default_graph())
b = tf.constant([2.0, 3.0], name="b")
result = a + b

sess = tf.Session()
sess.run(result)
print(a.graph is tf.get_default_graph())
