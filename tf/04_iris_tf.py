from sklearn.datasets import load_iris
import tensorflow as tf
import numpy as np
iris=load_iris()


x_data = iris.data
y_data = iris.target

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(x_data, y_data, epochs=50)

pr = model.predict([[400, 3.65, 2], [750, 3.7, 3]])

# classification - discrete, regression - sequential



