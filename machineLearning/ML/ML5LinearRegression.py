
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,100) # sample random -5,5 by 100 datas

print(x)

# linear regression
a = 2
b = 1
y = a*x + b

plt.plot(x,y,'-r',label='y=2x+1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="upper left")
plt.title("Display y=2x+1")
plt.grid()
plt.show()