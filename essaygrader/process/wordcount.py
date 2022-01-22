# Word count
def length(essay: str) -> int:
    from nltk.tokenize import RegexpTokenizer
    return len(tokenizer.tokenize(essay))