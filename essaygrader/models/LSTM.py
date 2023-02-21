import numpy as numpy
import tensorflow as tf 

import pandas as pd 
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pickle

df = pd.read_feather('essaygrader/data/dataset.feather')

source = df.loc[df['Source Dependent Responses'] == 1]
pne = df.loc[df['Persuasive/Narrative/Expository'] == 1]

source_ms = source.loc[source['grade'] == 0]
source_hs = source.loc[source['grade'] == 1]

X = source_ms[['Average Word Length', 'percent_misspelled',
       'word_count', 'percent_key_words', 'sentcount',
       'score', 'percent_stop_words', 'vocabulary']]
y = source_ms['normalized_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

BUFFER_SIZE = 10000
BATCH_SIZE = 64

VOCAB_SIZE = 1000
encoder = tf.keras.layers.TextVectorization(
    max_tokens = VOCAB_SIZE)
encoder.adapt(train_dataset.map(lambda text, label: text))