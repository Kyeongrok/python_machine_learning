import pandas as pd
import tensorflow as tf
import numpy as np

df = pd.read_csv('gpascore.csv')
df = df.dropna()
x_data = df[['gre', 'gpa', 'rank']].values
y_data = df['admit'].values

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(np.array(x_data), np.array(y_data), epochs=100)

print(model.predict([[400, 3.65, 2], [750, 3.7, 3]]))
