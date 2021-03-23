import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_data=load_iris()

# X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.3, random_state=24) 
# print('iris_data.data:',len(iris_data.data), type(iris_data.data))
# print('X_train:',len(X_train))
# print(iris_data.DESCR)

from collections import Counter
print(iris_data.target)
cnt = Counter(iris_data.target)
print(cnt)