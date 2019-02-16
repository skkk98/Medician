import pandas as pd
import numpy as np
import itertools
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pickle
import  os



def training(sample):
    data = pd.read_csv('/home/kalyan/PycharmProjects/Medician/Patient/insurance.csv')
    data.head()
    data1 = [data]


    # In[3]:


    #print (data1)


    # In[4]:


    gender_map = {'female': 1, 'male': 0}
    for dataset in data1:
        dataset['sex'] = dataset['sex'].map(gender_map)


    # In[5]:


    data.head(5)


    # In[6]:


    smoker_map = {'yes': 1, 'no': 0}
    for dataset in data1:
        dataset['smoker'] = dataset['smoker'].map(smoker_map)

    data.head(5)


    # In[7]:


    # region_map = {'southwest': 1, 'southeast': 2, 'northwest': 3, 'northeast': 4}
    # for dataset in data1:
    #     dataset['region'] = dataset['region'].map(region_map)

    # data.head(5)


    # In[8]:


    # from sklearn.preprocessing import OneHotEncoder
    # onehot = OneHotEncoder(categorical_features=[5])1


    # In[9]:


    #data = pd.get_dummies(data,prefix=['region'])
    #data.head(5)


    # In[10]:


    x = data[['age', 'sex', 'bmi', 'children', 'smoker']]
    y = data[['charges']]


    # In[11]:


    #print (x)


    # In[12]:


    # b = data.iloc[6: 10]
    #print (y)


    # In[13]:


    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)


    # In[14]:


    sc_x = StandardScaler()
    sc_y = StandardScaler()
    x_train = sc_x.fit_transform(x_train)
    x_test = sc_y.fit_transform(x_test)

    pkl_filename2 = "pickle_scaler.pkl"
    with open(pkl_filename2, 'wb') as file:
        pickle.dump(x, file)

    #print (x)
    #print (y)


    # In[15]:


    # regressor = RandomForestRegressor(max_leaf_nodes=30,random_state=42,n_estimators=2000)
    # regressor.fit(x_train,y_train)


    # In[16]:


    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)


    # In[17]:



    rf.fit(x_train, y_train)
    # [[18, 0, 45.500,2, 1]]
    y_predicted = rf.predict(sample)
    print(y_predicted)

    score = rf.score(x_test, y_test)
    print (score)

    pkl_filename = "pickle_model.pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump(rf, file)
    return y_predicted

def predict(data):
    pkl_filename = "pickle_model.pkl"
    pkl_filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), pkl_filename)
    with open(pkl_filename, 'rb') as file:
        rf = pickle.load(file)


    pkl_filename2 = "./pickle_scaler.pkl"
    pkl_filename2 = os.path.join(os.path.abspath(os.path.dirname(__file__)), pkl_filename2)
    with open(pkl_filename2, 'rb') as file:
        sc = pickle.load(file)


    y_predicted = rf.predict(data)
    print(y_predicted)
    return y_predicted
    #score = rf.score(x_test, y_test)
    #print (score)

if __name__ == "__main__":
    training()
