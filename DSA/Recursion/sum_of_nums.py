# Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

class Solution:
    def sumOfSeries(self,n):
        def sum_of_series(sum,n):
            if n == 0:
                return sum
            return sum_of_series(sum+(n**3),n-1)
        return sum_of_series(0,n)

sol = Solution()
print(sol.sumOfSeries(5))

# Time Complexity : O(n)
# Space Complexity : O(n)