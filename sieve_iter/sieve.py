#This is the .py file part

class sieve_i(object):
        def __init__(self):
           self.list = [2]
           self.size = 1

        def __iter__(self):
           return self

        def next(self):
  	   apd = self.list[-1]
	   while 1:      
             if self._is_prime(self.list,apd):
                self.list.append(apd)
		self.size+=1 
           	return self.list
	     apd +=1
        def _is_prime(self, primes, n):
           for i in primes:
                 if n % i == 0:
                    return False
           return True
