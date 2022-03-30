import tensorflow as tf

height = 170
foot_size = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)

def loss_function():
    expect_value = height * a * b
    return tf.square(260 - expect_value) # 오차

opt = tf.keras.optimizers.Adam(learning_rate=0.1)
opt.minimize(loss_function, var_list=[a, b])

