# Average sentence length of essays
def averageSentenceLength(essay):
    sents = essay.split(". ")
    return sum([len(i.split(" ")) for i in sents])/len(sents)