# -*- coding: utf-8 -*-

from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Activation, Dense
import pandas as pd
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

X_train.shape

y_train.shape

X_test.shape

y_test.shape

X_train = X_train.reshape(60000,28*28)

X_test = X_test.reshape(10000,28*28)

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

y_test

model = Sequential()
model.add(Dense(100,activation='relu', input_shape = (28*28,)))
model.add(Dense(100,activation='relu'))
model.add(Dense(10 , activation = 'softmax'))

model.compile(optimizer='adam', loss = 'categorical_crossentropy' , metrics = ['accuracy'])

y_train

model.fit (X_train,y_train, epochs = 15 , batch_size = 20)

history = model.fit(X_train,y_train,epochs=5,batch_size=128)

model.evaluate(X_test, y_test)

model.evaluate(X_train, y_train)

print(model.summary())

plt.plot(history.history['loss'])
plt.title('Model Loss')

plt.plot(history.history['accuracy'])
plt.title('Model Accuracy')

