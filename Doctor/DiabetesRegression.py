
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import itertools
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# In[2]:

def training(sample):
    data = pd.read_csv('/home/kalyan/PycharmProjects/Medician/Doctor/diabetes.csv')
    data.head()
    data1 = [data]
    x = data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
    y = data[['Outcome']]


    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

    sc_x = StandardScaler()
    sc_y = StandardScaler()
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_y.fit_transform(x_test)

    lr = LogisticRegression()
    lr.fit(x_train, y_train)
    # prediction part
    y_predicted = lr.predict(x_test)
    #print (y_predicted)
    y = lr.predict(sample)
    print(y)
    score = lr.score(x_test, y_test)
    print ("Accuracy :-", score)
    return y[0],score
    '''diabetic = []
    for i in range(0, len(y_predicted)):
        if y_predicted[i] == 0 :
            diabetic.append( "Non Diabetic :)")
        elif y_predicted[i] == 1 :
            diabetic.append("Diabetic..!!")'''


'''def pred()
    y_predicted = lr.predict(x_test)
    print (y_predicted)
    score = lr.score(x_test, y_test)
    print ("Accuracy :-", score)
    diabetic = []
    for i in range(0, len(y_predicted)):
        if y_predicted[i] == 0 :
            diabetic.append( "Non Diabetic :)")
        elif y_predicted[i] == 1 :
            diabetic.append("Diabetic..!!")'''
