# Count the number of digits.

from math import *

class Solution:
    def count_digits(self, x: int) -> int:
        temp = abs(x)
        y = 0
        while temp>0:
            y+=1
            temp = temp//10
        return y

        # Time Complexity: O(log10(n))
    
    def count_digits_optimized(self, x: int) -> int:
        temp = abs(x)
        return int(log10(temp) + 1)

sol = Solution()
print(sol.count_digits(654654))
print(sol.count_digits_optimized(654654))