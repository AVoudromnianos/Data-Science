"""
@author: AposV
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn.metrics import accuracy_score,precision_score

#---------------------------------------------------------
#Part A
Sum = 0
#MAIN PROGRAM
names=['Pregnancies','Glucose','BloodPressure',
       'SkinThickness','Insulin','BMI',
       'DPF','Age','Outcome']

dataset = pd.read_csv("diabetes.csv", names=names)

for i in range(0,len(dataset)):
    for j in range(1,8):
        if dataset.iloc[i,j] == 0:
            for k in range(0,len(dataset)):
                Sum += dataset.iloc[k,j] 
            dataset.iloc[i,j]= Sum/k
            Sum = 0

dataset.to_csv("diabetes_missing_values_replace.csv",float_format="%.2f") 

dataset1 = pd.read_csv("diabetes_missing_values_replace.csv")

#DIVIDE dataset to x,y
X=dataset1.drop(['Pregnancies','Outcome'],axis=1)
Y=dataset1['Outcome']

k= 5
scores=[]
Accuracy_list1=[]
precision_list=[]

for i in range(20):
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20)

    knn= KNeighborsClassifier(n_neighbors=k, metric= 'minkowski')
    knn.fit(X_train, Y_train)
    
    #predict label of test  data
    Y_pred= knn.predict(X_test)
    Accuracy_list1.append(metrics.accuracy_score(Y_test, Y_pred))
    precision_list.append(metrics.precision_score(Y_test,Y_pred))
    
print('Accuracy list 1 k=5\n', Accuracy_list1)

#K 1-15
k_range= range(1,16)
scores=[]
accuracyA=[]
precision_list=[]

for k in k_range:
    knn= KNeighborsClassifier(n_neighbors=k, metric= 'minkowski')
    knn.fit(X_train, Y_train)

    #predict label of test  data
    Y_pred= knn.predict(X_test)
    accuracyA.append(metrics.accuracy_score(Y_test, Y_pred))
    precision_list.append(metrics.precision_score(Y_test,Y_pred))

print('Accuracy list A(K == 1-15)\n', accuracyA)

#---------------------------------------------------------
#Part B

dataset = pd.read_csv("final_dataset.csv")

X=dataset.drop(['Pregnancies','Outcome'],axis=1)
Y=dataset['Outcome']

k= 5
scores=[]
Accuracy_list2=[]
precision_list=[]

for i in range(20):
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20)

    knn= KNeighborsClassifier(n_neighbors=k, metric= 'minkowski')
    knn.fit(X_train, Y_train)
    
    #predict label of test  data
    Y_pred= knn.predict(X_test)
    Accuracy_list2.append(metrics.accuracy_score(Y_test, Y_pred))
    precision_list.append(metrics.precision_score(Y_test,Y_pred))
    
print('Accuracy list 2 k=5\n', Accuracy_list2)

#K 1-15
k_range= range(1,16)
scores=[]
accuracyB=[]
precision_list=[]

for k in k_range:
    knn= KNeighborsClassifier(n_neighbors=k, metric= 'minkowski')
    knn.fit(X_train, Y_train)

    #predict label of test  data
    Y_pred= knn.predict(X_test)
    accuracyB.append(metrics.accuracy_score(Y_test, Y_pred))
    precision_list.append(metrics.precision_score(Y_test,Y_pred))
    
print('Accuracy list B(K=1-15)\n', accuracyB)


print("\nAccuracy_A= \n",accuracyA)
print('Max accuracyA= ', max(accuracyA))
print('Min accuracyA= ',min(accuracyA))

print("\nAccuracy_Β= \n",accuracyB)
print('Max accuracyB= ', max(accuracyB))
print('Min accuracyB= ',min(accuracyB))

#---------------------------------------------------------
#Part C

DeviationA= max(accuracyA)-min(accuracyA)
DeviationB= max(accuracyB)-min(accuracyB)
if DeviationA > DeviationB:
    print('accuracyB is more accurate than accuracyA')
elif Deviation A < DeviationB:
    print('accuracyA is more accurate than accuracyB')
else:
    print('They have equal accuracy')
