import tensorflow as tf
import numpy as np

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(2, input_dim=1))
model.add(tf.keras.layers.Dense(1))
model.compile(loss='mse', optimizer='sgd')

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3.5, 4, 5])
x_test = np.array([5, 6, 7, 8])

model.fit(x, y, epochs=40)

print(model.predict(x_test))
