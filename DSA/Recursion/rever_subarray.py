# Given an array arr, you need to reverse a subarray of that array. The range of this subarray is given by indices l and r (1-based indexing).


# Brute force approach:
class Solution:
	def reverseSubArray(self,arr,l,r):
		arr2 = []
		for i in range(l-1,r):
			arr2.append(arr[i])
		for i in range(l-1, r):
			val = arr2.pop()
			arr[i] = val
		return arr
	
sol = Solution()
print(sol.reverseSubArray([1, 2, 3, 4, 5], 2, 4))
print(sol.reverseSubArray([8,2,5,3,1,7,8,4,5], 3, 7))

# Efficient approach: (Recursion)
class Solution:
	def reverseSubArray(self, arr, l, r):
		if l >= r:
			return arr
		temp = arr[l-1]
		arr[l-1] = arr[r-1]
		arr[r-1] = temp
		return self.reverseSubArray(arr, l+1, r-1)

sol = Solution()
print(sol.reverseSubArray([1, 2, 3, 4, 5], 2, 4))
print(sol.reverseSubArray([8,2,5,3,1,7,8,4,5], 3, 7))

# Time Complexity : O(n)
# Space Complexity : O(n) 
		