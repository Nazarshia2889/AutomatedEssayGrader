# Average sentence length of essays
def averageSentenceLength(essay):
    sents = essay.split(".")
    return sum([len(i) for i in sents.split(" ")])/len(sents)