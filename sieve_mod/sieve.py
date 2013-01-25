
#This is a .py file of module style to implement Eratosthenes' Sieve

_primelist = [2]

def _is_prime(primes, n):
	for i in primes:
		if n % i == 0:
			return False
	return True

def sieve(n):
	global _primelist
	start = _primelist[-1] +1
	size = 1
	while size < n :
		if _is_prime(_primelist, start):
			_primelist.append(start)
			size+=1
		start += 1
	return _primelist



