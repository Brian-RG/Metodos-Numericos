def cumulative_sum(lst):
	if(len(lst) >0):
		for e in range(1,len(lst)):
			lst[e]+=lst[e-1]
	return lst
