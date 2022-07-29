import seaborn as sb
import matplotlib.pyplot as plt

iris_dataset = sb.load_dataset('iris')

print(iris_dataset.head()) # show first 5 rows

print(iris_dataset.tail()) # show last 5 rows

sb.set()
sb.pairplot(iris_dataset,hue='species',size=2)
plt.show()