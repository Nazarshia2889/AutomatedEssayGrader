# percent of key nouns from prompt in essay
def keyWords(keyWords, essay):
    import nltk
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(keyWords)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    count = 0
    for i in nouns:
        count += list(essay).count(i.lower())
        count += list(essay).count(i.capitalize())
        count += list(essay).count(i.lower() + 's')
        count += list(essay).count(i.capitalize() + 's')
    result = round(((count/len(essay))*100), 2)
    return result