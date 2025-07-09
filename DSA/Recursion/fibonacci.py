# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 

class Solution:
    def func(self, num):
        if num == 0 or num == 1:
            return num
        return self.func(num-1) + self.func(num-2)
    def fib(self, n: int) -> int:
        res = self.func(n)
        return res
    
sol = Solution()
print(sol.fib(0))  # Output: 0
print(sol.fib(1))  # Output: 1
print(sol.fib(2))  # Output: 1
print(sol.fib(3))  # Output: 2
print(sol.fib(4))  # Output: 3
print(sol.fib(5))  # Output: 5

# Time Complexity: O(2^n) - Exponential time complexity due to the recursive calls.
# Space Complexity: O(2^n) - The recursion stack can go as deep as n, leading to a space complexity of O(n) for the call stack.