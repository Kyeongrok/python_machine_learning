import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import model_selection, linear_model
from sklearn.metrics import mean_squared_error
import os

os.chdir(os.path.dirname(__file__))
df_data = pd.read_excel('boston_house_data.xlsx', index_col=0) # 엑셀 파일 읽기
df_target = pd.read_excel('boston_house_target.xlsx', index_col=0)

# 1. Prepare the data (array!)
boston_data = np.array(df_data)
boston_target = np.array(df_target)

# 2. Feature selection
boston_X = boston_data[:, 8:9]
boston_Y = boston_target

# 3. Train/Test split
x_train, x_test, y_train, y_test = model_selection.train_test_split(boston_X, boston_Y, test_size=0.3, random_state=0)

# 4. Create model object
model = linear_model.LinearRegression()

# 5. Train the model
model.fit(x_train, y_train)

# 6. Test the model
print('MSE(Training data) : ', mean_squared_error(model.predict(x_train), y_train))
print('MSE(Test data) : ', mean_squared_error(model.predict(x_test), y_test))

# 7. Visualize the model
plt.figure(figsize=(10, 10))
plt.scatter(x_test, y_test, color="black") # Test data
plt.scatter(x_train, y_train, color="red", s=1) # Train data
plt.plot(x_test, model.predict(x_test), color="blue", linewidth=3) # Fitted line
plt.show()
# print(model.predict(x_test))