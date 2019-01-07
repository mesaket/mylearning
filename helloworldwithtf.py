import tensorflow as tf

value = tf.constant("Here I am!!")

sess = tf.session()

print(sess.run(value)

sess.close()
