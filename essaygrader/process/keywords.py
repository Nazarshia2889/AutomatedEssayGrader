def keyWords(keyWords, essay):
    import nltk
    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(keyWords)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
    count = 0
    for i in nouns:
        count += essay.count(i.lower())
        count += essay.count(i.capitalize())
    result = round(((count/len(essay))*100), 2)
    return result