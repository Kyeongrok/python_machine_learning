from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris_data=load_iris()
dt = DecisionTreeClassifier()

dt.fit(iris_data.data, iris_data.target)
print(dt)

pred = dt.predict([[6.5, 3.,  5.2, 2. ]])
print(pred)
