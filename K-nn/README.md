# Diabetes CSV

## A part
  1. Preprocessing data in diabetes.csv
  2. Searching for zeros or null values and replace them with the average value of the feature. Then this will be saved in diabetes_missing_values_replace.csv.
  3. Uses a k-nn classifier to sort the samples of diabetes_missing_values_replace with k=5.
  4. Uses accuracy metric.
  5. Reapeat the experiment 20 times. We need to see if our model is stable or not.
  6. It runs with k == 1-15 and create a table accuracyA with accuracy values.

## B part
  1. Use a k-nn classifier to sort the samples of finaldataset.csv with k= 5.
  2. Use accuracy metric
  3. Reapeat the experiment 20 times to see if our model is stable or not.
  4. We run it with k == 1-15 and create a table accuracyB with accuracy values.
  
## C part
   ``` Compare the results of accuracyA with accuracyB```

  Report
|Accuracy_A|Accuracy|
|:--:|:--:|
|0.6493506493506493, 0.6753246753246753, 0.6623376623376623|Min = 0.6493506493506493|
|0.6883116883116883, 0.7207792207792207, 0.7207792207792207|------------|
|0.7467532467532467, 0.7402597402597403, 0.7077922077922078|------------|
|0.7012987012987013, 0.7207792207792207, 0.7142857142857143|------------|
|0.7467532467532467, 0.7272727272727273, 0.7272727272727273|Max= 0.7467532467532467|

|Accuracy_Β|Accuracy|
|:--:|:--:|
|0.6075949367088608, 0.6708860759493671, 0.7341772151898734|Min = 0.6075949367088608|
|0.6962025316455697, 0.6962025316455697, 0.6835443037974683|------------|
|0.7468354430379747, 0.6962025316455697, 0.6835443037974683|Max = 0.7468354430379747|
|0.6582278481012658, 0.6708860759493671, 0.6455696202531646|------------|
|0.6835443037974683, 0.6708860759493671, 0.6708860759493671|------------|


Deviation of A = about 10%

Deviation of B = about 14%

```Deviation resulting from Max accuracy - Min accuracy.```

Comparing the values of two tables, accuracyA-table is more stable than accuracyB-table because: 
1. Max value is closer to 100%
2. Deviaton of A value is less than Deviation of B
