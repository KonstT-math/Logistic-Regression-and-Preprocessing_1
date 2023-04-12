import numpy as np
import pandas as pd
from lreg import LogisticRegression

test_length = 900

nofeats = 13

# -----------------------------------------

# data:

# the following csv file has all nan values filled (see preprocess0.py)
#data1 = pd.read_csv('fr_nan_free.csv')
# the following csv file has all rows containing nan values deleted (see preprocess2.py)
#data1 = pd.read_csv('fr_nan_free_rows.csv')

# the following csv file is nan value free, and also is in standard scale (see preprocess1.py)
data1 = pd.read_csv('fr_std.csv')

#print(data1)

# use significance.py to decide which features will participate
data = data1.drop(data1.columns[[3,13]],axis = 1)

#print(data)

data = np.array(data)
m,n = data.shape

np.random.shuffle(data)

data_test = data[0:test_length]
X_test = data_test[:,0:nofeats]
Y_test = data_test[:,nofeats]
#Y_test = Y_test.reshape(1,-1)
Y_test = Y_test.T

data_train = data[test_length:m]
X_train = data_train[:, 0:nofeats] 
Y_train = data_train[:,nofeats] 
#Y_train = Y_train.reshape(1,-1)
Y_train = Y_train.T

#print(X_train.shape, Y_train.shape)

# -----------------------------------------

def accuracy(y_pred, y_test):
	return np.sum(y_pred==y_test)/len(y_test)

classifier = LogisticRegression()
classifier.fit(X_train , Y_train)
y_pred = classifier.predict(X_test)

print("real :",Y_test)
print("predicts: ",y_pred)

acc = accuracy(y_pred, Y_test)
print(acc)


