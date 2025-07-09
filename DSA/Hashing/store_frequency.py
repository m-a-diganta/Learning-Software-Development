# Store the frequency of number in a list

def store_frequency(arr):
    freq = {}
    for i in arr:
        if i not in freq.keys():
            freq[i] = 1
        else:
            freq[i] += 1
    return freq

print("Frequency of each number:", store_frequency([1, 2, 3, 4, 5, 1, 2, 3]))

# Time Complexity: O(n) => time complexity to find a key in deictionary is O(1) on average
# Space Complexity: O(n)


# Method 2

def store_frequency2(arr):
    hash_map = dict()
    for i in range(len(arr)):
        hash_map[arr[i]] = hash_map.get(arr[i], 0) + 1 # get() method returns the value for the specified key if key is in dictionary, else default value (0 in this case)
    return hash_map

print("Frequency of each number:", store_frequency2([1, 2, 3, 4, 5, 1, 2, 3]))