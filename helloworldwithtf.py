import tensorflow as tf

value = tf.constant("Here I am!!")

sess = tf.Session()

print(sess.run(value)

sess.close()
