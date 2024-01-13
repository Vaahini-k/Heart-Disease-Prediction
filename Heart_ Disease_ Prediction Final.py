# for numerical computing
import numpy as np


# for dataframes
import pandas as pd


#for plotting
import matplotlib.pyplot as plt
import seaborn as sns



# Ignore Warnings
import warnings
warnings.filterwarnings("ignore")



# to split train and test set
from sklearn.model_selection import train_test_split



# Machine Learning Models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier


from sklearn.metrics import accuracy_score




# to save the final model on disk

data=pd.read_csv('heart.csv')
print(data.shape)

info = ["age","1: male, 0: female","chest pain type, 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic","resting blood pressure"," serum cholestoral in mg/dl","fasting blood sugar > 120 mg/dl","resting electrocardiographic results (values 0,1,2)"," maximum heart rate achieved","exercise induced angina","oldpeak = ST depression induced by exercise relative to rest","the slope of the peak exercise ST segment","number of major vessels (0-3) colored by flourosopy","thal: 3 = normal; 6 = fixed defect; 7 = reversable defect"]



for i in range(len(info)):
    print(data.columns[i]+":\t\t\t"+info[i])
    


print(data.columns)
print(data.head())
print(data.describe())
print(data.corr())


data = data.drop_duplicates()
print( data.shape )


print(data.isnull().sum())
data=data.dropna()
print(data.isnull().sum())




data["target"].value_counts().plot(kind="bar", color=["salmon","lightblue"])
plt.xlabel("0 = No Disease, 1 = Disease")
plt.title("Heart Disease")
plt.show()



# Create a plot of crosstab
pd.crosstab(data.target, data.sex).plot(kind="bar",
                                    figsize=(10,6),
                                    color=["salmon","lightblue"])
plt.title("Heart Disease Frequency for Sex")
plt.xlabel("0 = No Disease, 1 = Disease")
plt.legend(["Female","Male"])
plt.show()





y = data.target

# Create separate object for input features
X = data.drop('target', axis=1)




# Split X and y into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.2, random_state=0)



# Print number of observations in X_train, X_test, y_train, and y_test
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)



model1= LogisticRegression()
model2=RandomForestClassifier(random_state=285) #285,1673
model3= KNeighborsClassifier(n_neighbors=9)
model4=DecisionTreeClassifier()
model5= GaussianNB()
model6=SVC(kernel='linear',C=10 ,gamma=0.0009)
model7=XGBClassifier()



model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
model3.fit(X_train, y_train)
model4.fit(X_train, y_train)
model5.fit(X_train, y_train)
model6.fit(X_train, y_train)
model7.fit(X_train, y_train)




## Predict Test set results
y_pred1 = model1.predict(X_test)
y_pred2 = model2.predict(X_test)
y_pred3 = model3.predict(X_test)
y_pred4 = model4.predict(X_test)
y_pred5 = model5.predict(X_test)
y_pred6 = model6.predict(X_test)
y_pred7 = model7.predict(X_test)





acc1 = accuracy_score(y_test, y_pred1) ## get the accuracy on testing data
print("Accuracy of Logistic Regression is {:.2f}%".format(acc1*100))



acc2 = accuracy_score(y_test, y_pred2)  ## get the accuracy on testing data
print("Accuracy of RandomForestClassifier is {:.2f}%".format(acc2*100))



acc3 = accuracy_score(y_test, y_pred3)  ## get the accuracy on testing data
print("Accuracy of KNeighborsClassifier is {:.2f}%".format(acc3*100))



acc4 = accuracy_score(y_test, y_pred4)  ## get the accuracy on testing data
print("Accuracy of Decision Tree is {:.2f}%".format(acc4*100))



acc5 = accuracy_score(y_test, y_pred5) ## get the accuracy on testing data
print("Accuracy of GaussianNB is {:.2f}%".format(acc5*100))



acc6 = accuracy_score(y_test, y_pred6)  ## get the accuracy on testing data
print("Accuracy of SVC is {:.2f}%".format(acc6*100))



acc7 = accuracy_score(y_test, y_pred7)  ## get the accuracy on testing data
print("Accuracy of XGB Classifier is {:.2f}%".format(acc6*100))




#from sklearn.externals import joblib 
import joblib

# Save the model as a pickle in a file 
joblib.dump(model2, 'heart_disease.pkl') 
  
# Load the model from the file 
final_model = joblib.load('heart_disease.pkl')


pred=final_model.predict(X_test)


acc = accuracy_score(y_test,pred)# get the accuracy on testing data
print("Final Model Accuracy is {:.2f}%".format(acc*100))






scores = [acc1,acc2,acc3,acc4,acc5,acc6,acc7]
algorithms = ["Logistic Regression","Random Forest","KNN","Decision Tree","Naive Bayes","SVC","XGB Classifier"]    


sns.set(rc={'figure.figsize':(15,8)})
plt.xlabel("Algorithms")
plt.ylabel("Accuracy score")

sns.barplot(algorithms,scores)

plt.show()




