#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Import my dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout
import os
import tensorflow as tf


# In[39]:


df = pd.read_csv(r'C:\Users\riddz\Desktop\AAPL.csv')
df.head()


# In[40]:


#preprocessing our data
df = df['open'].values
df = df.reshape(-1,1)
print(df.shape)
df[:7]


# In[42]:


dataset_train = np.array(df[:int(df.shape[0]*0.8)])
dataset_test = np.array(df[int(df.shape[0]*0.8)-50:])
print(dataset_train.shape)
print(dataset_test.shape)


# In[43]:


scaler = MinMaxScaler(feature_range=(0,1))
dataset_train = scaler.fit_transform(dataset_train)
dataset_train[:7]


# In[44]:


dataset_test = scaler.transform(dataset_test)
dataset_test[:7]


# In[45]:


def create_my_dataset(df):
    x = []
    y = []
    for i in range(50,df.shape[0]):
        x.append(df[i-50:i,0])
        y.append(df[i,0])
    x = np.array(x)
    y = np.array(y)
    return x,y


# In[47]:


x_train, y_train = create_my_dataset(dataset_train)
x_train[:1]


# In[48]:


y_train[:1]


# In[49]:


x_test, y_test = create_my_dataset(dataset_test)
x_test[:1]


# In[50]:


#reshaping for LSTM
x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1],1))
print(x_train.shape)
print(x_test.shape)


# In[61]:


tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
model = Sequential()
model.add(LSTM(units=96, return_sequences=True, input_shape=(x_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(units=96, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=96))
model.add(Dropout(0.2))
model.add(Dense(units=1))


# In[62]:


model.summary()


# In[68]:


model.compile(loss='mean_squared_error', optimizer ='adam')


# In[69]:


if(not os.path.exists(r'C:\Users\riddz\Desktop\stock_prediction.riddhesh')):
    model.fit(x_train, y_train, epochs=50, batch_size=32)
    model.save(r'C:\Users\riddz\Desktop\stock_prediction.riddhesh')


# In[65]:


model = load_model(r'C:\Users\riddz\Desktop\stock_prediction.riddhesh')


# In[66]:


#visualizing our predictions
get_ipython().run_line_magic('matplotlib', 'inline')
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

fig, ax = plt.subplots(figsize=(8,4))
plt.plot(df, color='red', label='original Stockprice')
ax.plot(range(len(y_train)+50, len(y_train)+50+len(predictions)),predictions,color='blue', label='predicted')
plt.legend()
print(range(len(y_train)+50, len(y_train)+50+len(predictions)))


# In[67]:


y_test_scaled = scaler.inverse_transform(y_test.reshape(-1,1))

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(y_test_scaled, color='red', label = 'True Price of testing set')
plt.plot(predictions, color = 'blue', label='predicted')
plt.legend()

