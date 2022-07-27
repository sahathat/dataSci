from scipy.io import loadmat
import matplotlib.pyplot as plt

mnist_raw = loadmat("D:\Benz\Resources\DBMS\dataSci\machineLearning\ML\mnist-original.mat")

mnist = {
    "data": mnist_raw["data"].T,
    "target": mnist_raw["label"][0]
}

print(mnist["data"])

print(mnist["data"].shape)

# 0-69999
index = 10001

x,y = mnist["data"],mnist["target"]

number = x[index]
number_image = number.reshape(28,28)

print(y[index])

plt.imshow(number_image,cmap=plt.cm.binary,interpolation="nearest")

plt.show()

