
from re import A
import numpy as np
import matplotlib.pyplot as plt

ran = np.random
x = ran.rand(50)*10
a = 2
b = ran.randn(50) # ran negative and postive value between -1 to 1
y = a*x+b
print(y)

plt.scatter(x,y)
plt.plot(x,2*x+1,'-r',label='y=2x+1')
plt.xlabel('x')
plt.ylabel('y')
plt.show()