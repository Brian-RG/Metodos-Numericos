def removeDups(lst):
	lista=[]
	for e in lst:
		if(e not in lista):
			lista.append(e)
	
	return lista
