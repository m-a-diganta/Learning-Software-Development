# Recursion => when a function calls itself
# Infinite recursion => desn't stop => stack overflow error

# Head recursion
def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print(n)    
head_recursion(3)

print("\n========================\n")

# Tail Recursion
def tail_recursion(n):
    if n == 0:
        return
    print(n)
    tail_recursion(n - 1)
    
tail_recursion(3)


# Time Complexity : O(n)
# Space Complexity : O(n)