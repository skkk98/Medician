#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten


# In[2]:


classifier = Sequential()


# In[3]:


#convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))


# In[4]:


#Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))


# In[5]:


#flattening
classifier.add(Flatten())


# In[6]:


#Full Connection
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1, activation = 'sigmoid'))


# In[7]:


#Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# In[8]:


#Fitting the CNN to image
from keras.preprocessing.image import ImageDataGenerator


# In[9]:


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)


# In[10]:


test_datagen = ImageDataGenerator(rescale=1./255)


# In[11]:


training_set = train_datagen.flow_from_directory(
                                                'training_set',
                                                target_size=(64, 64),
                                                batch_size=32,
                                                class_mode='binary')


# In[12]:


test_set = test_datagen.flow_from_directory(
                                            'test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')


# In[13]:


classifier.fit_generator(
                    training_set,
                    steps_per_epoch=230,
                    epochs=10,
                    validation_data=test_set,
                    validation_steps=28)


# In[ ]:




