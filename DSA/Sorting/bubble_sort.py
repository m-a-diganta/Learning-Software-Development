# Given an array, arr[]. Sort the array using bubble sort algorithm.

class Solution:
    def bubbleSort(self,arr):
        is_swap = False # For best case scenario, if arr already sorted
        for i in range(len(arr)):
            for j in range(len(arr)-1):
                if arr[j+1] < arr[j]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_swap = True
            if is_swap == False:
                return arr
        return arr

sol = Solution()
print(sol.bubbleSort([4, 1, 3, 9, 7]))
print(sol.bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(sol.bubbleSort([38, 20, 31, 20, 14, 30]))
print("\n")

# Time Complexity = O(N^2) [in Best case => O(N)]
# Space Complexity = O(1)

# Let's do this in descending order

class Solution: 
    def bubbleSort(self, arr):
        is_swap = False # For best case scenario, if arr already sorted
        for i in range(len(arr)):
            for j in range(len(arr)-1):
                if arr[j+1] > arr[j]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_swap = True
            if is_swap == False:
                return arr
        return arr

sol = Solution()
print(sol.bubbleSort([4, 1, 3, 9, 7]))
print(sol.bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(sol.bubbleSort([38, 14, 31, 20, 14, 30]))