# test of model use

# Import Libraries
import pandas as pd
import numpy as np 
from statistics import mean
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pickle

# Import other functions
from process.averageWordLength import averageWordLength
from process.misspellings import nmisspelled
from process.wordcount import length
from process.averageSentenceLength import averageSentenceLength
from process.grammarchecker import grammarCheck
from process.keywords import keyWords
from process.sentcount import sentcount
from process.vocabulary import VocabCounter
from process.stopwords import stopWords
from models.explainability import explain

# Import models
regressor_source_ms = pickle.load(open('essaygrader/model_files/regressor_source_ms.sav', 'rb'))
regressor_source_hs = pickle.load(open('essaygrader/model_files/regressor_source_hs.sav', 'rb'))
regressor_pne_ms = pickle.load(open('essaygrader/model_files/regressor_pne_ms.sav', 'rb'))
regressor_pne_hs = pickle.load(open('essaygrader/model_files/regressor_pne_hs.sav', 'rb'))

# Ask for grade and topic
school = input("Are you in middle school or high school? (MS/HS): ")
topic = input("Is your essay Source Dependent or Persuasive/Narrative/Expository? (SD/PNE): ")
essay = input("Input your essay: ")
prompt = input("Input the prompt: ")

# Adding features
tokenizer = RegexpTokenizer(r'\w+')
cleanedessay = tokenizer.tokenize(essay)

stop_words = set(stopwords.words('english'))
cleanedessay_nosw = [w for w in cleanedessay if not w.lower() in stop_words]

features = []
features.append(averageWordLength(cleanedessay))
features.append(nmisspelled(cleanedessay))
features.append(length(cleanedessay))
features.append(keyWords(prompt, cleanedessay_nosw))
features.append(sentcount(essay))
# Repastes imagery function
def evaluate(essay):
    emote = pd.read_excel('essaygrader/data/pastData/emote.xlsx')
    points = 0
    for word in essay:
        word = word.lower()
        if word.lower() in emote['word'].unique():
            bnoun = emote[emote['word'] == word]['noun'].values[0]
            if (bnoun):
                points += mean(emote[emote['word'] == word][['ndim' + str(i) for i in range(1, 8)]].values[0])
            else:
                points += mean(emote[emote['word'] == word][['adim' + str(i) for i in range(1, 11)]].values[0])

    return points
features.append(evaluate(cleanedessay))
features.append(stopWords(cleanedessay))
def vocabulary(li):
    vocab = VocabCounter()
    return round(vocab.CountVocab(li)*100, 2)
features.append(vocabulary(cleanedessay))


row = pd.DataFrame([features], columns=['Average Word Length', 'percent_misspelled', 'word_count', 'percent_key_words', 'sentcount', 'score', 'percent_stop_words', 'voccabulary'])

# Split by grade and topic
df = pd.read_feather('essaygrader/data/dataset.feather')

source = df.loc[df['Source Dependent Responses'] == 1]
pne = df.loc[df['Persuasive/Narrative/Expository'] == 1]

source_ms = source.loc[source['grade'] == 0]
source_hs = source.loc[source['grade'] == 1]
pne_ms = pne.loc[pne['grade'] == 0]
pne_hs = pne.loc[pne['grade'] == 1]

# explainability
explain_source_ms = explain(row, source_ms)
explain_pne_ms = explain(row, pne_ms)
explain_source_hs = explain(row, source_hs)
explain_pne_hs = explain(row, pne_hs)

# Run model and give feedback
if school == 'MS':
    if topic == 'SD':
        print("Grade prediction: ", regressor_source_ms.predict(row)[0])

        print(explain_source_ms.checkAverageWordLength())
        print(explain_source_ms.checkMisspelled())
        print(explain_source_ms.checkLength())
        print(explain_source_ms.checkKeyWords())
        print(explain_source_ms.checkVocabulary())
        print(explain_source_ms.checkPercentStopWords())
    else:
        print("Grade prediction: ", regressor_pne_ms.predict(row)[0])

        print(explain_pne_ms.checkAverageWordLength())
        print(explain_pne_ms.checkMisspelled())
        print(explain_pne_ms.checkLength())
        print(explain_pne_ms.checkKeyWords())
        print(explain_pne_ms.checkVocabulary())
        print(explain_pne_ms.checkPercentStopWords())
else:
    if topic == 'SD':
        print("Grade prediction: ", regressor_source_hs.predict(row)[0])

        print(explain_source_hs.checkAverageWordLength())
        print(explain_source_hs.checkMisspelled())
        print(explain_source_hs.checkLength())
        print(explain_source_hs.checkKeyWords())
        print(explain_source_hs.checkVocabulary())
        print(explain_source_hs.checkPercentStopWords())
    else:
        print("Grade prediction: ", regressor_pne_hs.predict(row)[0])

        print(explain_pne_hs.checkAverageWordLength())
        print(explain_pne_hs.checkMisspelled())
        print(explain_pne_hs.checkLength())
        print(explain_pne_hs.checkKeyWords())
        print(explain_pne_hs.checkVocabulary())
        print(explain_pne_hs.checkPercentStopWords())
