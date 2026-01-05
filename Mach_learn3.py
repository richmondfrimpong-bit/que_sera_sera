from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd


digit = load_digits()
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))
for item in zip(axes.ravel(), digit.images, digit.target):
    axes, image, target = item
    axes.imshow(image)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)
plt.tight_layout()
plt.show()

knn = KNeighborsClassifier()
new_sv = SVC(gamma='scale')
gaush = GaussianNB()
est_ors = [knn, new_sv, gaush]
for est in est_ors:
    kfold = KFold(n_splits= 10, shuffle= True, random_state= 11)
    score = cross_val_score(estimator=est, X=digit.data, y=digit.target, cv=kfold)
    print(f'{est}_Average performance : {score.mean():.2%}')
    print(f'{est}_Standard_Deviation : {score.std():.2%}')


X_train, X_test, y_train, y_test = train_test_split(digit.data, digit.target, random_state=11, shuffle=True)
newme = new_sv.fit(X=X_train, y=y_train)
predicted = new_sv.predict(X=X_test)
expected = y_test
conf = confusion_matrix(y_true=expected, y_pred=predicted)
conf_gra = pd.DataFrame(conf, index=range(10), columns=range(10))
print(conf)
report = classification_report(y_true=expected, y_pred=predicted)
print(report)

sns.heatmap(conf_gra, annot=True, cmap='nipy_spectral_r')
plt.show()
