# You are given an integer n. You have  to print all numbers from 1 to n.

class Solution:    
    def printNos(self,n):
        def printnumbers(i,n):
            if (i>n):
                return
            print(i, end=' ')
            printnumbers(i+1,n)
        printnumbers(1, n)
sol = Solution()
sol.printNos(5)

# Time Complexity : O(n)
# Space Complexity : O(n)