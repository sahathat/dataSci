from pyexpat import model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv("ML\Weather.csv")

print(dataset.shape) # (119040,31)

print(dataset.describe()) # summary

# train test set
x = dataset['MinTemp'].values.reshape(-1,1)
y = dataset['MaxTemp'].values.reshape(-1,1)

# separate 80% - 20%
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.2,random_state=0)

# training
model=LinearRegression()
model.fit(x_train,y_train)

# test
y_predict = model.predict(x_test)

# prdict test
# plt.scatter(x_test,y_test)
# plt.plot(x_test,y_predict,color="red",linewidth=2)
# plt.title('Min and Max temperature')
# plt.xlabel('min temp')
# plt.ylabel('max temp')
# plt.show()

# compare true data & predict data
df = pd.DataFrame({'Actually':y_test.flatten(),'Predicted':y_predict.flatten()}) # flatten() change array 2D to 1D

print(df.head())

print(df.shape) # (23808, 2)

# df20 = df.head(20)
# df20.plot(kind="bar",figsize=(16,10)) # plot bar chart by dataframe
# plt.show()

# performace checking
print("MAE =",metrics.mean_absolute_error(y_test,y_predict)) # 3.1993291783785835
print("MSE =",metrics.mean_squared_error(y_test,y_predict)) # 17.631568097568532
print("RMSE =",np.sqrt(metrics.mean_squared_error(y_test,y_predict))) # 4.198996082109215

# r-square percent
print("Score = ",metrics.r2_score(y_test,y_predict)) # 0.7670218843587753 
