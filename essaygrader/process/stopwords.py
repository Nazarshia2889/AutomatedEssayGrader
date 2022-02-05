# percentage of stop words
# Takes in an essay (list of words) and returns percentage of stop words
def stopWords(essay):
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    
    stop_words = set(stopwords.words('english'))
    return round((len([w for w in essay if w.lower() in stop_words])/len(essay))*100, 2)