# Total number of sentences
def sentcount(essay):
    from nltk import tokenize
    return len(tokenize.sent_tokenize(essay))