from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()

features = iris.data ## this are features
labels = iris.target ## this are labels

print(features[0],labels[0])


# Training the classifer
clf = KNeighborsClassifier()
clf.fit(features,labels)

# testing the model by giving values by ourself
preds = clf.predict([[31,1,1,1]])
print(preds)


