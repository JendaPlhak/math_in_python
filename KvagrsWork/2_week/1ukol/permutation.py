def permutation(d_list):
	if len(d_list) == 1:
		return [d_list]
	else:	
		total = []
		for x in d_list:
			tmpList = list(d_list) # Jedna moznost, druha tmpList = d_list[:], tmpList = d_list na sebe jen odkazuje
			tmpList.remove(x)
			for sigma in permutation(tmpList):
				sigma.insert(0,x)
				total.append(sigma)
		return total

# d_list[:] je ekvivaletni d_list[0:len(d_list)]

def combination(d_list, length):
	if len(d_list) == 1:
		return [d_list]
	else:
		
	pass

lst = ['a','b','c','d']
lst2 = ['a','b']

print permutation(lst2)
print len(permutation(lst2	))

# What does .remove() do?
#print lst
#lst.remove('a')
#print lst
