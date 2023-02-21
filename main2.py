from statistics import mean

import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from essaygrader.process.averageWordLength import averageWordLength
from essaygrader.process.misspellings import nmisspelled
from essaygrader.process.wordcount import length
from essaygrader.process.averageSentenceLength import averageSentenceLength
from essaygrader.process.grammarchecker import grammarCheck
from essaygrader.process.keywords import keyWords
from essaygrader.process.sentcount import sentcount
from essaygrader.process.vocabulary import VocabCounter
from essaygrader.process.stopwords import stopWords
from eg import essaygrader

import streamlit as st

import pandas as pd

nltk.download('all')

st.title('Automated Essay Grader')

grade = st.radio('Essay Type', ['Middle School', 'High School'])
topic = st.radio('What kind of essay did you write?', ['Source Dependent', 'Persuasive/Narrative/Expository'])
prompt = st.text_input('Essay Prompt')
essay = st.text_area('Essay')

def cleanEssay(essay):
	essays = [essay]
	tokenizer = RegexpTokenizer(r'\w+')
	cleanedessay = tokenizer.tokenize(essay)
	essays.append(cleanedessay)
	stop_words = set(stopwords.words('english'))
	cleanedessay_nosw = [w for w in cleanedessay if not w.lower() in stop_words]
	essays.append(cleanedessay_nosw)
	return essays

def makeFeatures(essays, prompt):
	essay = essays[0]
	cleanedessay = essays[1]
	cleanedessay_nosw = essays[2]
	features = []
	features.append(averageWordLength(cleanedessay))
	features.append(nmisspelled(cleanedessay))
	features.append(length(cleanedessay))
	features.append(keyWords(prompt, cleanedessay_nosw))
	features.append(sentcount(essay))
	features.append(evaluate(cleanedessay))
	features.append(stopWords(cleanedessay))
	features.append(vocabulary(cleanedessay))
	row = pd.DataFrame([features], columns=['Average Word Length', 'percent_misspelled', 'word_count', 'percent_key_words', 'sentcount', 'score', 'percent_stop_words', 'vocabulary'])
	return row

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

def vocabulary(li):
	vocab = VocabCounter()
	return round(vocab.CountVocab(li)*100, 2)

if st.button('Submit'):
	essays = cleanEssay(essay)
	row = makeFeatures(essays, prompt)

	grader = essaygrader(grade, topic, row)
	answer = grader.gradeEssay()
	prediction = answer[0:25]
	feedback = answer[25:]

	st.write(prediction)
	st.write(feedback)