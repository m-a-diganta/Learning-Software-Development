# Find out if a number is armstrong number or not.

from math import *
class Solution:
    def armstrong(self, x: int) -> int:
        temp = abs(x)
        y = 0
        number_of_digits = int(log10(temp)+1)
        while temp>0:
            y = ((temp%10)**number_of_digits) + y
            temp = temp//10
        return x==y

sol = Solution()
print(sol.armstrong(153))
print(sol.armstrong(1634))




# Time Complexity: O(log10(n))