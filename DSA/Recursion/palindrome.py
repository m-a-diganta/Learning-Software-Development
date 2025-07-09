# You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

class Solution:
	def isPalindrome(self, s: str) -> bool:
		l = 0
		r = len(s) - 1
		def check_palindrome(l, r, s):
			if l >= r:
				return True
			if s[l] != s[r]:
				return False
			return check_palindrome(l + 1, r - 1, s)

		return check_palindrome(l, r, s)

sol = Solution()
print(sol.isPalindrome("madam"))  # True
print(sol.isPalindrome("hello"))  # False
print(sol.isPalindrome("racecar"))  # True

# Time Complexity: O(n) ~ O(n/2) 
# Space (Stack cause recursion) Complexity: O(n) ~ O(n/2)