"""
@author: AposV
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn.metrics import accuracy_score

def average(lst): 
    return sum(lst) / len(lst) 

def pososto(score):
    return "{0:.2f}%".format(score * 100)
    
#MAIN PROGRAM
data = 'breast-cancer-wisconsin.csv'
names=['Sample code number','Clump Thickness ',
       'Uniformity of Cell Size','Uniformity of Cell Shape',
       'Marginal Adhesion ','Single Epithelial Cell Size',
       'Bare Nuclei','Bland Chromatin',
       'Normal Nucleoli', 'Mitoses','Class']
breast= pd.read_csv(data, names= names)

for i in range(len(breast)-1,-1,-1):
    for j in range(0,11):
        if breast.iloc[i,j] == '?':
            breast = breast.drop([breast.index[i]],axis=0)
            break

#DIVIDE dataset to x,y
X=breast.drop(['Sample code number','Class'],axis=1)
Y=breast['Class']

#preprocessing
data_scaler= preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled= data_scaler.fit_transform(X)

#acccuracy 
A_score=[]

for i in range(20):
  X_train,X_test,Y_train,Y_test=train_test_split(data_scaled,Y,test_size=0.20)
  svclassifier=SVC(kernel='rbf')
  svclassifier.fit(X_train,Y_train)
  
  Y_pred=svclassifier.predict(X_test)
  A_score.append(metrics.accuracy_score(Y_test,Y_pred))

print(confusion_matrix(Y_test,Y_pred))
print(classification_report(Y_test,Y_pred))
print('Loops = ', i+1)
print('Min accuracy score = ', pososto(min(A_score)))
print('Max accuracy score = ', pososto(max(A_score)))
print('Average accuracy score  = ', pososto(average(A_score)))
print('Percentage Deviation = ', pososto((max(A_score)-min(A_score))))

#Is it stable?
if (max(A_score)-min(A_score)) <= 0.06:
    print('Stable')
else:
    print('Unstable')
#-------------------------------------------------------------------------
