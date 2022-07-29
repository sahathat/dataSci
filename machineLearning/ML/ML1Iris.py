from sklearn import datasets

iris_dataset = datasets.load_iris()

print(iris_dataset['data']) # all data

print(iris_dataset['data'][0:10]) # first 10 row data

print(iris_dataset.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])

from sklearn.model_selection import train_test_split

# defualt 75%, 25%
# (150,4)
x_train,x_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset["target"],test_size=.3,random_state=0)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# 150
# train 75% = floor(150*.75) = 112
# test 25% = floor(150*.25) + 1 = 38
# train 70% = 105
# test 30% = 45