import tensorflow as tf
import os

train_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"
test_dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv"

train_dataset_fp = tf.keras.utils.get_file(fname=os.path.basename(train_dataset_url), origin=train_dataset_url)
test_path = tf.keras.utils.get_file(fname=os.path.basename(test_dataset_url), origin=test_dataset_url)

print("데이터셋이 복사된 위치: {}".format(train_dataset_fp))
print("데이터셋이 복사된 위치: {}".format(test_path))
# tf.keras.utils.get_file(fname=os)