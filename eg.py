# Import Libraries
import pandas as pd
import numpy as np 
from statistics import mean
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pickle
from essaygrader.models.explainability import explain

# Import models
regressor_source_ms = pickle.load(open('essaygrader/model_files/regressor_source_ms.sav', 'rb'))
regressor_source_hs = pickle.load(open('essaygrader/model_files/regressor_source_hs.sav', 'rb'))
regressor_pne_ms = pickle.load(open('essaygrader/model_files/regressor_pne_ms.sav', 'rb'))
regressor_pne_hs = pickle.load(open('essaygrader/model_files/regressor_pne_hs.sav', 'rb'))

# Essay grader
class essaygrader():

    def __init__(self, grade, topic, row):
        self.grade = grade
        self.topic = topic
        self.row = row
        self.df = pd.read_feather('essaygrader/data/dataset.feather')
        self.source = self.df.loc[self.df['Source Dependent Responses'] == 1]
        self.pne = self.df.loc[self.df['Persuasive/Narrative/Expository'] == 1]
        self.source_ms = self.source.loc[self.source['grade'] == 0]
        self.source_hs = self.source.loc[self.source['grade'] == 1]
        self.pne_ms = self.pne.loc[self.pne['grade'] == 0]
        self.pne_hs = self.pne.loc[self.pne['grade'] == 1]
        self.explain_source_ms = explain(self.row, self.source_ms)
        self.explain_pne_ms = explain(self.row, self.pne_ms)
        self.explain_source_hs = explain(self.row, self.source_hs)
        self.explain_pne_hs = explain(self.row, self.pne_hs)

    def gradeEssay(self):
        self.answer = ""
        if self.grade == 'MS':
            if self.topic == 'SD':
                self.answer += "Grade prediction: " + str(round(regressor_source_ms.predict(self.row)[0], 2)) + "%. "
                self.answer += self.explain_source_ms.checkAverageWordLength() + " "
                self.answer += self.explain_source_ms.checkMisspelled() + " "
                self.answer += self.explain_source_ms.checkLength() + " "
                self.answer += self.explain_source_ms.checkKeyWords() + " "
                self.answer += self.explain_source_ms.checkVocabulary() + " "
                self.answer += self.explain_source_ms.checkPercentStopWords() + " "
                return self.answer
            else:
                self.answer += "Grade prediction: " + str(round(regressor_pne_ms.predict(self.row)[0], 2)) + "%. "
                self.answer += self.explain_pne_ms.checkAverageWordLength() + " "
                self.answer += self.explain_pne_ms.checkMisspelled() + " "
                self.answer += self.explain_pne_ms.checkLength() + " "
                self.answer += self.explain_pne_ms.checkKeyWords() + " "
                self.answer += self.explain_pne_ms.checkVocabulary() + " "
                self.answer += self.explain_pne_ms.checkPercentStopWords() + " "
                return self.answer
        else:
            if self.topic == 'SD':
                self.answer += "Grade prediction: " + str(round(regressor_source_hs.predict(self.row)[0], 2)) + "%. "
                self.answer += self.explain_source_hs.checkAverageWordLength() + " "
                self.answer += self.explain_source_hs.checkMisspelled() + " "
                self.answer += self.explain_source_hs.checkLength() + " "
                self.answer += self.explain_source_hs.checkKeyWords() + " "
                self.answer += self.explain_source_hs.checkVocabulary() + " "
                self.answer += self.explain_source_hs.checkPercentStopWords() + " "
                return self.answer
            else:
                self.answer += "Grade prediction: " + str(round(regressor_pne_hs.predict(self.row)[0], 2)) + "%. "
                self.answer += self.explain_pne_hs.checkAverageWordLength() + " "
                self.answer += self.explain_pne_hs.checkMisspelled() + " "
                self.answer += self.explain_pne_hs.checkLength() + " "
                self.answer += self.explain_pne_hs.checkKeyWords() + " "
                self.answer += self.explain_pne_hs.checkVocabulary() + " "
                self.answer += self.explain_pne_hs.checkPercentStopWords() + " "
                return self.answer
