#Repetition (not currently in use)
import nltk
nltk.download()

def repeat(essay: str) -> int:
    from nltk.corpus import stopwords
    sw = stopwords.words("english")
    