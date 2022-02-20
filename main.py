# import regular libraries
import pandas as pd
import numpy as np 
from statistics import mean
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import pickle
import nltk
from flask import request
from flask import jsonify
from flask import Flask, render_template

# Import other functions
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

app = Flask(__name__)

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


@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/input', methods=['POST'])
def my_form_post():
    grade = request.form.get('grade', None)
    topic = request.form.get('type', None)
    essay = request.form['text']
    prompt = request.form['text2']
    if (grade is not None) and (topic is not None) and (essay != "") and (prompt != ""):
        # grade = request.form['grade']
        # topic = request.form['type']
        # essay = request.form['text']
        # prompt = request.form['text2']
        essays = cleanEssay(essay)
        row = makeFeatures(essays, prompt)

        grader = essaygrader(grade, topic, row)
        answer = grader.gradeEssay()
        prediction = answer[0:25]
        feedback = answer[25:]

        return render_template('score.html', grade=prediction, explain=feedback)
    else:
        return render_template('input.html', error="Please fill in all required fields.")

if __name__ == "__main__":
    app.run(port='8088',threaded=False)