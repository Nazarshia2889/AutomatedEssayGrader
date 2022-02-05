# Import Libraries
import pandas as pd
import numpy as np

#Counts % of essay which contains vocab words
#Input a 1d or 2d array or embedded list of words

vocabwordsall = np.load('vocabularywords.npy')

class VocabCounterException(Exception):
    pass

class VocabCounter():

    def __init__(self):
        self.essay2d = None
        self.essay1d = None

    def CountVocab(self,input_essay2d):
        self.essay2d = input_essay2d

        #Convert embedded lists to np arrays
        if type(self.essay2d) == list:
            self.essay2d = np.array(self.essay2d)

        elif type(self.essay2d) == np.ndarray:
            pass

        #If input is not a list or array, raise an exception
        else:
            raise VocabCounterException("Input is not of type list or np.ndarray")

        self.essay1d = self.essay2d.flatten()

        NumVocabWords = 0
        for i in self.essay1d:
            if i in vocabwordsall:
                NumVocabWords +=1
                
        return NumVocabWords/len(self.essay1d)
