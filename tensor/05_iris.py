import tensorflow as tf
import pandas as pd
import numpy as np

train_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"

iris = pd.read_csv(train_dataset_url, header=0)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = iris.rename(columns={"120":'sepal_length', '4':'sepal_width', 'setosa':'petal_length', 'versicolor':'petal_width', 'virginica':'species'})

x_data = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
y_data = iris['species'].values

# Model 만들기
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.relu),
    tf.keras.layers.Dense(1)
])

model.compile(loss='categorical_crossentropy', metrics='accuracy')

# 학습 시키기
model.fit(np.array(x_data), np.array(y_data), epochs=10)

# 예측 하기
print(model.predict(x_data[:5]))