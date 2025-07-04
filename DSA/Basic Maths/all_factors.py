# Print All Factors of a Given Number

class Solution:
    def all_factors(self, x: int) -> int:
        factors = []
        for i in range(1,x+1):
            if (x%i==0):
                factors.append(i)
        return factors


sol = Solution()
print(sol.all_factors(15))

# Time complexity => O(n)
# Space Complexity => O(k) => k = total number of factors


# Optimized Solution
import math
class Solution:
    def all_factors_optimized(self, x: int) -> int:
        factors = []
        for i in range(1,(int(math.sqrt(x))+1)):
            if (x%i==0):
                factors.append(i)
                if (x//i) != i:
                    factors.append(x//i)
        factors.sort()
        return factors


sol = Solution()
print(sol.all_factors_optimized(15))
print(sol.all_factors_optimized(36))

# Time complexity => O(sqrt(n)) + O(nlogn)
# Space Complexity => O(k) => k = total number of factors