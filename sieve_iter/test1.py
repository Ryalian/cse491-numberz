import sieve


def test1():
	f = sieve.sieve_i()
	while f.size < 10:
		f.next()
	print f.list

test1()
