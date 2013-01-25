import sieve

print "Test if 233 is a prime"
print ""

for x, y in zip(range(233), sieve.sieve_g()):
	list = y

for i in list:
	if i == 233:
		print "233 is prime"
		Flag = 1
		break
if Flag != 1 :
	print "Damn! 233 is not prime!"

#Test if one specific number is prime
