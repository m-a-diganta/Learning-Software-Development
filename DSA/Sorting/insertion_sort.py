# The task is to complete the insertsort() function which is used to implement Insertion Sort.

class Solution:
    def insertionSort(self,arr):
        for i in range(len(arr)-1):
            if arr[i] > arr [i+1]:
                for j in range(i,-1,-1):
                    if arr[j+1] < arr[j]:
                        arr[j+1], arr[j] = arr[j], arr[j+1]
                    else:
                        break
        return arr

sol = Solution()
print(sol.insertionSort([4, 1, 3, 9, 7]))
print(sol.insertionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(sol.insertionSort([38, 20, 31, 20, 14, 30]))
print("\n")

# Time Complexity = O(N^2) [in Best case => O(N)]
# Space Complexity = O(1)