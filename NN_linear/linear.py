import tensorflow as tf
from tensorflow import keras

import pandas as pd
import numpy as np

train_df= pd.read_csv('train.csv')
# np.random.shuffle(train_df.values)

# print(train_df.head(5))

# # print(train_df.x.values[0:5])
# # print(type(train_df.x.values))

# model =keras.Sequential([
#     keras.layers.Dense(4,input_shape=(2,),activation='relu'),
#     keras.layers.Dense(2,activation='sigmoid')])

# model.compile(optimizer='adam',
#               loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])

# x=np.column_stack((train_df.x.values,train_df.y.values))

# model.fit(x,train_df.color.values ,batch_size=4)
