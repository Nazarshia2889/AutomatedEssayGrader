# Imagery score
import pandas as pd
import swifter
from statistics import mean

from concurrent.futures import ThreadPoolExecutor

df = pd.read_feather('essaygrader/data/essays.feather')
emote = pd.read_excel('essaygrader/data/emote.xlsx')

# def score(essay):
def score(essays):
	"""
	Scores an essay based on the emotion.
	"""

	iessay = 0
	scores = []

	def evaluate(essay):
		points = 0
		for word in essay.split():
			word = word.lower()
			if word.lower() in emote['word'].unique():
				bnoun = emote[emote['word'] == word]['noun'].values[0]
				if (bnoun):
					points += mean(emote[emote['word'] == word][['ndim' + str(i) for i in range(1, 8)]].values[0])
				else:
					points += mean(emote[emote['word'] == word][['adim' + str(i) for i in range(1, 11)]].values[0])

		return points

	with ThreadPoolExecutor(max_workers=64) as executor:
		for essay in essays:
			scores.append(executor.submit(evaluate, essay).result())
			iessay += 1
			print(iessay)

	return scores

df['score'] = score(df['essay'])
df.to_feather('imagery.feather')