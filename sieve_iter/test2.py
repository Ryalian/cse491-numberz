import sieve


def test2():
	f = sieve.sieve_i()
	while f.size < 10:
		f.next()
	list = f.list
	print "Test if expect number shows in sequence"
	print ""
	assert list[1]  == 3
	print "assert list[1] == 3: Seccess"
	assert list[2]  == 5
        print "assert list[2] == 5: Seccess"

test2()
