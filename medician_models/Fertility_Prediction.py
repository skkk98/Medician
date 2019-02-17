#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


data = pd.read_csv('fertility.csv')
data.head(5)


# In[3]:


# data.head()


# In[4]:


data = data.iloc[:, 1:]
data1 = [data]
# data.head(5)

# data.isnull().values.any()

# data = data[np.isfinite(data['Accident or serious trauma'])]
# data = data[np.isfinite(data['Surgical intervention'])]
# data = data[np.isfinite(data['High fevers in the last year'])]
# data = data[np.isfinite(data['Frequency of alcohol consumption'])]
# data = data[np.isfinite(data['Smoking habit'])]
# data = data[np.isfinite(data['Number of hours spent sitting per day'])]
# data = data[np.isfinite(data['Diagnosis'])]
# data = data[np.isfinite(data['Childish diseases'])]
# data = data[np.isfinite(data['Age'])]

data.dropna(subset=['Accident or serious trauma'],inplace=True)
data.dropna(subset=['Surgical intervention'],inplace=True)
data.dropna(subset=['High fevers in the last year'],inplace=True)
data.dropna(subset=['Frequency of alcohol consumption'],inplace=True)
data.dropna(subset=['Smoking habit'],inplace=True)
data.dropna(subset=['Number of hours spent sitting per day'],inplace=True)
data.dropna(subset=['Diagnosis'],inplace=True)
data.dropna(subset=['Childish diseases'],inplace=True)
data.dropna(subset=['Age'],inplace=True)




data.head(5)


# In[5]:


disease_map = {'no': 0, 'yes': 1}
for dataset in data1:
    dataset['Childish diseases'] = dataset['Childish diseases'].map(disease_map)
    
# data.head(5)


# In[6]:


trauma_map = {'yes': 1, 'no': 0}
for dataset in data1:
    dataset['Accident or serious trauma'] = dataset['Accident or serious trauma'].map(trauma_map)
    
# data.head(5)


# In[7]:


surgical_map = {'yes': 1, 'no': 0}
for dataset in data1:
    dataset['Surgical intervention'] = dataset['Surgical intervention'].map(surgical_map)
    
# data.head(5)


# In[8]:


# data


# In[9]:


fever_map = {'more than 3 months ago': 0, 'less than 3 months ago': 1, 'no' : 0}
for dataset in data1:
    dataset['High fevers in the last year'] = dataset['High fevers in the last year'].map(fever_map)
    
# data.head(5)


# In[10]:


# data


# In[11]:


alcohol_map = {'hardly ever or never' : 0, 'once a week': 50, 'several times a week': 100}
for dataset in data1:
    dataset['Frequency of alcohol consumption'] = dataset['Frequency of alcohol consumption'].map(alcohol_map)
    
# data.head(5)


# In[12]:


smoking_map = {'never' : 0, 'occasional': 50, 'daily': 100}
for dataset in data1:
    dataset['Smoking habit'] = dataset['Smoking habit'].map(smoking_map)
    
# data.head(5)


# In[13]:


diagnosis_map = {'Normal' : 0, 'Altered': 1}
for dataset in data1:
    dataset['Diagnosis'] = dataset['Diagnosis'].map(diagnosis_map)
    
data.head(5)


# In[14]:


data.dropna(subset=['Accident or serious trauma'],inplace=True)
data.dropna(subset=['Surgical intervention'],inplace=True)
data.dropna(subset=['High fevers in the last year'],inplace=True)
data.dropna(subset=['Frequency of alcohol consumption'],inplace=True)
data.dropna(subset=['Smoking habit'],inplace=True)
data.dropna(subset=['Number of hours spent sitting per day'],inplace=True)
data.dropna(subset=['Diagnosis'],inplace=True)
data.dropna(subset=['Childish diseases'],inplace=True)
data.dropna(subset=['Age'],inplace=True)


# In[15]:


x = data.iloc[:, :8]
y = data.iloc[:, 8:]


# In[16]:


print (x)


# In[17]:


print (y)


# In[18]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


# In[19]:


from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
x = sc_x.fit_transform(x)
y = sc_y.fit_transform(y)

# print (x)
# print (y)


# In[20]:


from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(x_train, y_train)


# In[21]:


# a = [[]]
y_predicted = rf.predict(x_test)
# for i in y_predicted:
#     if i < 0.5:
#         y_predicted[i] = 0
#     elif i > 0.5:
#         y_predicted[i] = 1
print (y_predicted)


# In[32]:


prediction = []
for i in range(0, len(y_predicted)):
    if y_predicted[i] < 0.05:
        y_predicted[i] = 0
        prediction.append('Normal Prediction')
    elif y_predicted[i] >= 0.05:
        y_predicted[i] = 1
        prediction.append('Altered Prediction')
print (y_predicted)

for j in prediction:
    print (j)


# In[33]:


a = [[30, 0, 1, 1, 0, 50.0, 50, 16]]
p = rf.predict(a)
print(p)


# In[ ]:




