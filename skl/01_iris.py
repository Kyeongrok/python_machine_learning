import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

iris_data=load_iris()

# df_clf= DecisionTreeClassifier(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.3, random_state=24)

print(X_train)
print(len(X_train))
print(len(iris_data.data))
print(120/150 * 100)

df_data = pd.read_excel('boston_house_data.xlsx', index_col=0, encoding='utf-8') # 엑셀 파일 읽기