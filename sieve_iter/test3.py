import sieve


def test3(n):
	print "Test is a number is prime. Here we use 233"
	print ""
	f = sieve.sieve_i()
	while f.size < n:
		f.next()
	list = f.list
	for i in list:
		if i == n:
		   print n,"is prime"
		   flag = 1
		   break
	if flag !=1:
	  print "Damn!", n, "is not prime!"

test3(233)
