from sklearn import datasets

iris_dataset = datasets.load_iris()

print(iris_dataset['data']) # all data


print(iris_dataset['data'][0:10]) # first 10 row data

print(iris_dataset.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])