import sieve

print "Test if expect number shows in right spot"
print ""

for x, y in zip(range(10 - 1), sieve.sieve_g()):
	list = y

assert list[1] == 3
print "assert list[1] == 3: Success"

assert list[2] == 5
print "assert list[2] == 5: Success"



#testing if the sequence contain expected number
