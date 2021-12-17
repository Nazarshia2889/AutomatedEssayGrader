# Average word length of essays
def averageWordLength(essay):
    return sum([len(i) for i in essay])/len(essay)