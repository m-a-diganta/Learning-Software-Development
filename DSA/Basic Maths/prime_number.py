# Given a number n, determine whether it is a prime number or not.
# Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

import math
class Solution:
    def isPrime(self, n):
        divisible_count = 0
        for i in range(2,(int(math.sqrt(n))+1)):
            if (n%i==0):
                divisible_count+=1
        if (divisible_count == 0 and n!=1):
            return True
        else:
            return False

sol = Solution()
print(sol.isPrime(7))
print(sol.isPrime(11))