from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

#Checking data properties
digit = load_digits()
print(digit.DESCR)
print(digit.images[30])
print(digit.data.shape)
print(digit.target.shape)

#Visualizing data
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6,4))
for item in zip(axes.ravel(), digit.images, digit.target):
    axes, image, target = item
    axes.imshow(image,cmap='nipy_spectral_r')
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(target)
plt.tight_layout()
plt.show()

#Split data
X_train, X_test, y_train, y_test = train_test_split(digit.data, digit.target, random_state=11)

#Train data
knn = KNeighborsClassifier()
train_set = knn.fit(X=X_train, y=y_train)
print(train_set)

#test model
predicted = knn.predict(X=X_test)
expected = y_test
print(f'Sample of prediction = {predicted[:20]}')
print(f'Sample of Expected = {expected[:20]}')
wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]
print(wrong)

#checking for accuracy
print(f'The model has an accuracy of : {knn.score(X=X_test, y=y_test)}')
mod_conf = confusion_matrix(y_true=expected, y_pred=predicted)
print(mod_conf)
mod_report = classification_report(y_true=expected, y_pred=predicted)
print(mod_report)
sns.heatmap(mod_conf, annot=True, cmap='nipy_spectral_r')
plt.show()

#Multiple training and testing with KFold
k_split = KFold(n_splits=10, shuffle=True, random_state= 11)
score = cross_val_score(estimator=knn, X=X_train, y=y_train, cv=k_split)
print(f'The following are the scores: {score}')
print(f'The average model performance score = {score.mean():.2f}')
print(f'The standard deviation in performance = {score.std():.2f}')








