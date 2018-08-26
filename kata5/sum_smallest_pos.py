def sum_two_smallest_nums(lst):
	f=recpos(lst)
	s=recpos(lst)
	return f + s
	
def recpos(lst):
	num=lst.pop(lst.index(min(lst)))
	if num>=0:
		return num
	else:
		return recpos(lst)
