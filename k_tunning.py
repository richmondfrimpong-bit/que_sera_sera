from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_digits

digit = load_digits()
knn = KNeighborsClassifier()
for k in range(1, 20, 2):
    kfold = KFold(n_splits=10, shuffle=True, random_state=11)
    score = cross_val_score(estimator=KNeighborsClassifier(n_neighbors=k),
                            X=digit.data, y=digit.target, cv=kfold)
    print(f'Accuracy of k_neighbors @ {k} = {score.mean():.2%}  ->  Standard Deviation = {score.std():.2%}')
