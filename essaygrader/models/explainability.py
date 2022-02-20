import numpy as np
import pandas as pd 

class explain():

    def __init__(self, row, df):
        self.row = row
        self.df = df
    
    def checkAverageWordLength(self):
        if self.row['Average Word Length'].iloc[0] < self.df['Average Word Length'].mean():
            return "Try incorporating bigger words into your essay."
        else:
            return "Average word length is good."
    
    def checkMisspelled(self):
        if self.row['percent_misspelled'].iloc[0] > self.df['percent_misspelled'].median():
            return "Look for spelling mistakes in your essay."
        else:
            return "Minimal spelling mistakes."
    
    def checkLength(self):
        if (self.row['word_count'].iloc[0] < self.df['word_count'].median()) or (self.row['sentcount'].iloc[0] < self.df['sentcount'].median()):
            return "Try to make your essay longer."
        else:
            return "Essay is long enough."
    
    def checkKeyWords(self):
        if self.row['percent_key_words'].iloc[0] > self.df['percent_key_words'].quantile([0.75]).iloc[0]:
            return "Your essay may be referring to the prompt too much."
        elif self.row['percent_key_words'].iloc[0] < self.df['percent_key_words'].quantile([0.25]).iloc[0]:
            return "Your essay may not be referring to the prompt enough."
        else:
            return "Essay echoes the prompt well enough."
    
    def checkVocabulary(self):
        if (self.row['score'].iloc[0] < self.df['score'].median()) or (self.row['vocabulary'].iloc[0] < self.df['vocabulary'].median()):
            return "Try to incorporate more effective vocabulary into your essay."
        else:
            return "Good use of vocabulary."
    
    def checkPercentStopWords(self):
        if self.row['percent_stop_words'].iloc[0] > self.df['percent_stop_words'].mean():
            return "Try using less stop words (a, the, is, are, etc.)."
        else:
            return "Minimal use of stop words."
