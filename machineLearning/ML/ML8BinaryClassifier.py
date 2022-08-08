from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
import itertools
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score

def displayImage(x):
    plt.imshow(x.reshape(28,28),cmap = plt.cm.binary,interpolation="nearest")
    plt.show()

def displayPredict(clf,actually_y,x):
    print("Actually = ",actually_y)
    print("Predict = ",clf.predict([x])[0])

mnist_raw = loadmat("ML\mnist-original.mat")
mnist = {
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}

x,y = mnist["data"],mnist["target"]

# train & test set
# train 1-60000
# test 60001-70000
x_train,x_test,y_train,y_test = x[:60000],x[60000:],y[:60000],y[60000:]

print(x_train.shape) # (60000, 748)
print(x_test.shape) # (10000, 748)

# class 0-9

# check is class 0
# predict = 5000 -> model -> predict class is 0 ? true : false

# y_train = [0,0,...,9,...,9]
predict = 5
clf_num = 0
y_train_clf = (y_train==clf_num)
y_test_clf = (y_test==clf_num)
print(y_train_clf.shape,y_train_clf)

# SGD classifier
sgd_clf = SGDClassifier()
sgd_clf.fit(x_train,y_train_clf) # class 0

# show image
# displayImage(x_test[predict])

# show predict
# displayPredict(sgd_clf,y_test_clf[predict],x_test[predict])

# cross validation
# score=cross_val_score(sgd_clf,x_train,y_train_clf,cv=3,scoring="accuracy")
# print(score)

# confusion matrix
y_train_pred = cross_val_predict(sgd_clf,x_train,y_train_clf,cv=3)
cm = confusion_matrix(y_train_clf,y_train_pred)
print(cm)

def displayConfusionMatrix(cm,cmap=plt.cm.GnBu):
    classes=["Other Number","Number 0"]
    plt.imshow(cm,interpolation='nearest',cmap=cmap)
    plt.title("Confusion Matrix")
    plt.colorbar()
    trick_marks=np.arange(len(classes))
    plt.xticks(trick_marks,classes)
    plt.yticks(trick_marks,classes)
    thresh=cm.max()/2
    for i , j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        plt.text(j,i,format(cm[i,j],'d'),
        horizontalalignment='center',
        color='white' if cm[i,j]>thresh else 'black')
    plt.tight_layout()
    plt.ylabel('Actually')
    plt.xlabel('Prediction')
    plt.show()

# display confusion matrix
plt.figure()
displayConfusionMatrix(cm)

# Test set
y_test_pred = sgd_clf.predict(x_test)
print(classification_report(y_test_clf,y_test_pred))
print("Accuracy Score = ", round(accuracy_score(y_test_clf,y_test_pred) * 100,2))