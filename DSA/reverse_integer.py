# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        y = 0
        while temp>0:
            y = (temp%10) + y*10
            temp = temp//10
        if y >= 2**31:
            return 0
        elif x>0:
            return y
        else:
            return -y

sol = Solution()
print(sol.reverse(-143))


# Time Complexity: O(log10(n))