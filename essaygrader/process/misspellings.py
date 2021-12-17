# misspellings
import enchant
from nltk.tokenize import RegexpTokenizer
d = enchant.Dict("en_US")
def nmisspelled(essay: str) -> int:
	return sum([1 for word in tokenizer.tokenize(essay) if not d.check(word)])