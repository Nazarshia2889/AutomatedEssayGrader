# Linear regression model (preliminary)
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pickle


# import data and split into source dependent and persuasive/narrative/expository
df = pd.read_feather('essaygrader/data/dataset.feather')

source = df.loc[df['Source Dependent Responses'] == 1]
pne = df.loc[df['Persuasive/Narrative/Expository'] == 1]

# Source dependent
source_ms = source.loc[source['grade'] == 0]
source_hs = source.loc[source['grade'] == 1]

X = source_ms[['Average Word Length', 'percent_misspelled',
       'word_count', 'percent_key_words', 'sentcount',
       'score', 'percent_stop_words', 'vocabulary']]
y = source_ms['normalized_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

regressor_source_ms = LinearRegression()  
regressor_source_ms.fit(X_train, y_train)

r_sq = regressor_source_ms.score(X_test, y_test)
print('score - Source Dependent Responses (Middle School):', r_sq)
print('Coeffs: ', regressor_source_ms.coef_)

filename = 'regressor_source_ms.sav'
pickle.dump(regressor_source_ms, open(filename, 'wb'))

# -----

X = source_hs[['Average Word Length', 'percent_misspelled',
       'word_count', 'percent_key_words', 'sentcount',
       'score', 'percent_stop_words', 'vocabulary']]
y = source_hs['normalized_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

regressor_source_hs = LinearRegression()  
regressor_source_hs.fit(X_train, y_train)

r_sq = regressor_source_hs.score(X_test, y_test)
print('score - Source Dependent Responses (High School):', r_sq)
print('Coeffs: ', regressor_source_hs.coef_)

filename = 'regressor_source_hs.sav'
pickle.dump(regressor_source_hs, open(filename, 'wb'))

# -----

# persuasive/narrative/expository
pne_ms = pne.loc[pne['grade'] == 0]
pne_hs = pne.loc[pne['grade'] == 1]

X = pne_ms[['Average Word Length', 'percent_misspelled',
       'word_count', 'percent_key_words', 'sentcount',
       'score', 'percent_stop_words', 'vocabulary']]
y = pne_ms['normalized_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

regressor_pne_ms = LinearRegression()  
regressor_pne_ms.fit(X_train, y_train)

r_sq = regressor_pne_ms.score(X_test, y_test)
print('score - Persuasive/Narrative/Expository (Middle School):', r_sq)
print('Coeffs: ', regressor_pne_ms.coef_)

filename = 'regressor_pne_ms.sav'
pickle.dump(regressor_pne_ms, open(filename, 'wb'))

# -----

X = pne_hs[['Average Word Length', 'percent_misspelled',
       'word_count', 'percent_key_words', 'sentcount',
       'score', 'percent_stop_words', 'vocabulary']]
y = pne_hs['normalized_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

regressor_pne_hs = LinearRegression()  
regressor_pne_hs.fit(X_train, y_train)

r_sq = regressor_pne_hs.score(X_test, y_test)
print('score - Persuasive/Narrative/Expository (High School):', r_sq)
print('Coeffs: ', regressor_pne_hs.coef_)

filename = 'regressor_pne_hs.sav'
pickle.dump(regressor_pne_hs, open(filename, 'wb'))