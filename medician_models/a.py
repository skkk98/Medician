# import numpy.core.multiarray
import cv2
import numpy as np 
#Load the training image 
img = cv2.imread("digits3.png")
#Convert this Image in gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Now we split the image to 5000 cells, each 20x20 size
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
# Make it into a Numpy array. It size will be (50,100,20,20)
x = np.array(cells)

# Now we prepare train data and test data.
train = x[:,:50].reshape(-1,400).astype(np.float32)   # Size = (2500,400)

test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)
# Create labels for train and test data
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]

# train_labels = train_labels.reshape((train_labels.size,1))
# train = train.reshape((1, train.size))

test_labels = train_labels.copy()
# Initiate kNN, train the data, then test it with test data for k=5
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)


# In[ ]:


ret,result,neighbours,dist = knn.findNearest(test,k=5)
# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong

matches = result==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print (accuracy)


# In[ ]:


# save the kNN Model
np.savez('knn_data.npz',train=train, train_labels=train_labels)


# In[ ]:


#Load the kNN Model
with np.load('knn_data.npz') as data:
   print (data.files)
   train = data['train']
   train_labels = data['train_labels']
 
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels) 
  
test_img=cv2.imread("test.jpeg")
test_img =cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
test_img =cv2.resize(test_img, (20, 20)) 
x = np.array(test_img)
test_img = x.reshape(-1,400).astype(np.float32)
ret,result,neighbours,dist = knn.findNearest(test_img,k=1)

#Print the predicted number 

print (int(result))


# # New Data

# In[ ]:


#image = cv2.imread('test1.jpeg')
#def new(image):
#    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#    small = cv2.pyrDown(image)
#    cv2.imshow('gray', gray)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#    img = cv2.resize(gray, (80, 80))
#    cv2.imshow('resized', img)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#    cells = [np.hsplit(row,4) for row in np.vsplit(img ,1)]
#    x = np.array(cells)
#    y = x.reshape(-1,400).astype(np.int64)
#    return y

#new(image)
    # Size = (3500,400)

#with np.load('knn_data.npz') as data:
#    print (data.files)
#    train = data['train']
#    train_labels = data['train_labels']
# 
#knn = cv2.ml.KNearest_create()
#knn.train(train, cv2.ml.ROW_SAMPLE, train_labels) 
  
#test_img=cv2.imread("test1.jpeg")
#test_img =cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
#test_img =cv2.resize(test_img, (20, 20)) 
#x = np.array(test_img)
#test_img = x.reshape(-1,400).astype(np.float32)
#ret,result,neighbours,dist = knn.findNearest(test_img,k=1)
