from sklearn import model_selection
from sklearn.svm import SVC
from sklearn import metrics

import pandas as pd
glass=pd.read_csv("glass.csv")
X = glass.drop('Type',axis=1)
Y = glass['Type']
X_train,X_test,Y_train,Y_test=model_selection.train_test_split(X,Y,test_size=0.2)
model=SVC(kernel='rbf',gamma='auto')
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)
print("accuracy score:",metrics.accuracy_score(Y_test,Y_pred))
print(metrics.classification_report(Y_test, Y_pred))


