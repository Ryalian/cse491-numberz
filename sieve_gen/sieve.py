# This is the file for generator

def sieve_g():
	list = [2]
	size = 2

	
	while 1:
	   flag = 0
	   size += 1
	   for i in list:
		if size % i == 0:
		   flag = 1		  
	   if flag != 1:
		list.append(size)
		yield list

