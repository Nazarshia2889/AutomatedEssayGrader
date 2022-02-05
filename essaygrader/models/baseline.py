# Linear regression model (preliminary)
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# import data and split into source dependent and persuasive/narrative/expository
df = pd.read_feather('essaygrader/data/dataset.feather')
source = df.loc[df['Source Dependent Responses'] == 1]
pne = df.loc[df['Persuasive/Narrative/Expository'] == 1]

# Source dependent
X = source[['Average Word Length', 'misspelled',
       'word_count', 'key_words_count', 'sentcount',
       'score', 'percent_stop_words']]
y = source['normalized_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train)

r_sq = regressor.score(X_test, y_test)
print('score - Source Dependent Responses:', r_sq)

# persuasive/narrative/expository
X = pne[['Average Word Length', 'misspelled',
       'word_count', 'key_words_count', 'sentcount',
       'score', 'percent_stop_words']]
y = pne['normalized_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(X_train, y_train)

r_sq = regressor.score(X_test, y_test)
print('score - Persuasive/Narrative/Expository:', r_sq)

# import stastsmodels.api as sm

# model = sm.OLS(y, X)
# model.fit()
# print(model.summary())