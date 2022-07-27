import matplotlib.pyplot as plt
from sklearn import datasets

mnist_dataset = datasets.load_digits()

print(mnist_dataset.keys())
# dict_keys(['data', 'target', 'frame', 'feature_names', 'target_names', 'images', 'DESCR'])

print(mnist_dataset["images"].shape)

print(mnist_dataset.target_names)

print(mnist_dataset["images"][0]) # show array 2d of image

print(mnist_dataset["images"][0].shape) # show size of image px

plt.imshow(mnist_dataset.images[3], cmap=plt.get_cmap('RdYlGn')) # set image
plt.show() # show image

