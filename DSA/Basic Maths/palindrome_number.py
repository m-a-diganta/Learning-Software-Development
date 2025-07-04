# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        y = 0
        while temp>0:
            y = (temp%10) + y*10
            temp = temp//10
        if x==y:
            return True
        else:
            return False
        
sol = Solution()
print(sol.isPalindrome(-121))  
print(sol.isPalindrome(123))
print(sol.isPalindrome(523325))




# Time Complexity: O(log10(n))