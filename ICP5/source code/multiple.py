import pandas as pd
import numpy as np

train = pd.read_csv('winequality-red.csv')
df=train.replace(0.00,np.NaN)
data = df.fillna(train.mean())
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)
#print(data['citric acid'])
numeric_features = data.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print (corr['quality'].sort_values(ascending=False)[:10], '\n')
y = data['quality']
X = data.drop(['quality'], axis=1)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, random_state=42, test_size=.33)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
predictions = model.predict(X_test)
print ("R^2 is: \n", model.score(X_test, y_test))
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))
##correlation plot

from matplotlib import pyplot as plt
from matplotlib import cm as cm

fig = plt.figure()
ax1 = fig.add_subplot(111)
cmap = cm.get_cmap('jet', 30)
cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
ax1.grid(True)
plt.title('Correlation')
labels=['sulphates',  'citric acid ','fixed acidity','residual sugar','free sulfur dioxide','pH','chlorides','density']
fig.colorbar(cax, ticks=[.75, .8, .85, .90, .95, 1])
ax1.set_xticklabels(labels,fontsize=6)
ax1.set_yticklabels(labels,fontsize=6 )
plt.show()

correlation_matrix(df)

