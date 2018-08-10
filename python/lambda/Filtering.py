#Filtering words in a list
def isFourLetters(lst):
	lista=list(filter(lambda word: len(word)==4 , lst))
	return lista
