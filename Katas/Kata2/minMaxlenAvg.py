def minMaxLengthAverage(lst):
	lista=[]
	lista.append(min(lst))
	lista.append(max(lst))
	lista.append(len(lst))
	lista.append(sum(lst)/len(lst))
	return lista
