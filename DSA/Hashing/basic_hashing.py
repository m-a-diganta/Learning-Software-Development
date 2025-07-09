# n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10], m = [10, 111, 1, 9, 5, 67, 2] , Constraints: 1< n[i] < 10, n can have 10^8 elements, m can have 10^8 elements, Find the frequency of each element in m in n.

# Brute force approach:
def store_frequency(arr, m):
    for i in m:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        print(f"{i} => {count}", end=", ")

store_frequency([5, 3, 2, 2, 1, 5, 5, 7, 5, 10], [10, 111, 1, 9, 5, 67, 2])
print("\n")
    
# Time Complexity: O(n * m) => n is the length of arr and m is the length of m
# Space Complexity: O(1)

# Hashing approach:
def store_frequency_hash(arr, m):
    hash_list = [0]*11
    for i in arr:
        hash_list[i] += 1
    for i in m:
        if i> 10 or i < 1:
            print(f"{i} => 0", end=", ")
        else:
            print(f"{i} => {hash_list[i]}", end=", ")
store_frequency_hash([5, 3, 2, 2, 1, 5, 5, 7, 5, 10], [10, 111, 1, 9, 5, 67, 2])
# Time Complexity: O(n + m) => n is the length of arr and m is the length of m
# Space Complexity: O(1) => we are using a fixed size list of size 11


print("\n")
# Dictionary approach:
def store_frequency_dict(arr, m):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    for i in m:
        print(f"{i} => {freq.get(i, 0)}", end=", ")
store_frequency_dict([5, 3, 2, 2, 1, 5, 5, 7, 5, 10], [10, 111, 1, 9, 5, 67, 2])
# Time Complexity: O(n + m) => n is the length of arr and m is the length of m
# Space Complexity: O(n) => we are using a dictionary to store the frequency of elements in arr
