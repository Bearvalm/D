from sklearn import tree
import sklearn


# features = [[140, 'smooth'], [150, 0], [130, 'smooth'], [170, 'smooth'], [170, 'bumpy']]
# labels = ['apple', 'orange', 'apple', 'apple', 'orange']

features = [[140, 1], [150, 0], [130, 1], [170, 1], [170, 0]]
labels = [0, 1, 0, 0, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# clf = sklearn.neighbors.KNeighborsClassifier()
# clf = clf.fit(features, labels)

print(clf.predict([[151, 0]]))
