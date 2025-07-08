# Given a positive integer, n. Find the factorial of n.

class Solution:
    def factorial (self, n):
        def fact(total,n):
            if n == 0:
                return total
            return fact(total*n, n-1)
        return fact(1,n)

sol = Solution()
print(sol.factorial(5))

# Time Complexity : O(n)
# Space Complexity : O(n)

# Efficient solution 
class Solution:
    def factorial (self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)
sol = Solution()
print(sol.factorial(5))