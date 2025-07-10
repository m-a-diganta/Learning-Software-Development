# Given an array arr, use selection sort to sort arr[] in increasing order.

class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_ind = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[min_ind]:
                    min_ind = j
            arr[i], arr[min_ind] = arr[min_ind], arr[i]
        return arr

sol = Solution()
print(sol.selectionSort([4, 1, 3, 9, 7]))
print(sol.selectionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(sol.selectionSort([38, 20, 31, 20, 14, 30]))
print("\n")

# Time Complexity = O(N^2)
# Space Complexity = O(1)

# Let's do this in descending order

class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            max_ind = i
            for j in range(i+1,len(arr)):
                if arr[j] > arr[max_ind]:
                    max_ind = j
            arr[i], arr[max_ind] = arr[max_ind], arr[i]
        return arr

sol = Solution()
print(sol.selectionSort([4, 1, 3, 9, 7]))
print(sol.selectionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(sol.selectionSort([38, 14, 31, 20, 14, 30]))