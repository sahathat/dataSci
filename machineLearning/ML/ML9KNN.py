from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

iris_dataset = load_iris()
x_train,x_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],test_size=.4,random_state=0)

# Model
knn = KNeighborsClassifier(n_neighbors=10)

# train
knn.fit(x_train,y_train)

# test & predict
index = 1
y_pred = knn.predict([x_test[index]])
target_predict = iris_dataset['target_names'][y_pred]

print("result of predict: ", y_pred)
print("target of predict: ", target_predict)

# measure confusion matrix & precision recall
y_predicts = knn.predict(x_test)
print(classification_report(y_test,y_predicts,target_names=iris_dataset['target_names']))
print("accuracy = ", round(accuracy_score(y_test,y_predicts)* 100,2))