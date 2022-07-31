
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# data model
ran = np.random
x = ran.rand(50)*10
a = 2
b = ran.randn(50) # ran negative and postive value between -1 to 1
y = a*x+b
print(y)

# linear regression model
model=LinearRegression()

print(x)
x_new = x.reshape(-1,1)
print(x_new) # Fit shape to array 2D

# train model
model.fit(x_new,y) # train array 2D algorithm 

print(model.score(x_new,y))
# find r-square, coefficient
# if data have precision that r-square more than .95

# test model
xfit=np.linspace(-1,11)
print(xfit)
xfit_new=xfit.reshape(-1,1) # provide xfit array 2D algorithm 
print(xfit_new)

yfit = model.predict(xfit_new)

# analysis model & result
plt.scatter(x,y)
plt.plot(xfit,yfit,'-r',label='y=2x+1')
plt.title("Display Linear regression")
plt.xlabel('x')
plt.ylabel('y')
plt.show()