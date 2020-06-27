import os
import cv2
import numpy as np
import sklearn
import sklearn.model_selection
import matplotlib.pyplot as plt
import keras


datafolder='RockPaperScissors'
data=[]
labels=[]
folders=['Paper','Rock','Scissors']
for symbol in folders:
    path = os.path.join(datafolder,symbol)
    images=os.listdir(path)
    for eachImage in images:
        imgarray=cv2.imread(os.path.join(path,eachImage),cv2.IMREAD_GRAYSCALE)
        if eachImage != '.DS_Store':
            data.append(imgarray)
            if symbol == "Paper":
                labels.append(0)
            elif symbol=="Rock":
                labels.append(1)
            elif symbol=="Scissors":
                labels.append(2)
##        print(type(imgarray),eachImage)
##print(labels)
print(len(data))
print(len(labels))

data=np.array(data)
labels = np.array(labels)

train_images,test_images,train_labels,test_labels=sklearn.model_selection.train_test_split(data,labels,test_size=0.1)
class_names=["Rock","Paper","Scissors"]
train_images=train_images/255
test_images=test_images/255

print(test_images.shape)
print(train_images.shape)

#building the model(blueprint/design)
model=keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation='relu'), #activation if it passes certian threshold
    keras.layers.Dense(3,activation='softmax') #gives percentages for each number in third layer
    ])

#Compile the model/properties of model(giving extra features/personalizing)(gather raw materials to build)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics= ['accuracy'])

#Train the model(Building the house)
model.fit(train_images,train_labels,epochs=10)

#Test the model(Living in the house and checking if everything is fine)
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(test_acc)  #accuracy of test

#saving the model so we don't have to run it each time
model.save('savedRockPaperScissors.h5')

