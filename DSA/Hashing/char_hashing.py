# s = "azyxyyzaaaa", q = ["d", "a", "y", "x"], find the frequency of each character of q list in s string. 

def store_frequency_char(s, q):
    hash_map = [0] * (ord('z') - ord('a') + 1) 
    for char in s:
        hash_map[ord(char) - ord('a')] += 1
    for char in q:
        if ord(char) < ord('a') or ord(char) > ord('z'):
            print(f"{char} => 0", end=", ")
        else:
            print(f"{char} => {hash_map[ord(char) - ord('a')]}", end=", ")

store_frequency_char("azyxyyzaaaa", ["d", "a", "y", "x"])
print("\n")
# Time Complexity: O(n + m) => n is the length of s and m is the length of q
# Space Complexity: O(1) 




# s= "azYxAAzaaaa", q = ["d", "a", "A", "x"]
# Brute Force
def store_frequency_char(s, q):
    freq_map = [0]* ( (ord('z') - ord('a') + 1) + (ord('Z') - ord('A') + 1) )
    for char in s:
        if ord('a') <= ord(char) and  ord(char) <= ord('z'): 
            freq_map[ord(char)-ord('a')] += 1
        else:
            freq_map[ord(char)-ord('a') + (ord('a') - ord('Z')) - 1 ] += 1
    for i in q:
        if ord('a') <= ord(i) and  ord(i) <= ord('z'): 
            print(f"{i} => {freq_map[ord(i) - ord('a')]} ", end=", ")
        else:
            print(f"{i} => {freq_map[ord(i) - ord('a') + (ord('a') - ord('Z')) - 1 ]} ", end=", ")
store_frequency_char("azAxAYzaaaa", ["d", "a", "A", "x", "A", "Y", "z"])
print("\n")

# With Dictionary
def store_frequency_char(s, q):
    hash_map = {}
    for char in s:
        hash_map[char] = hash_map.get(char,0) + 1
    print(hash_map)

    for char in q:
        if char not in hash_map.keys():
            print(f"{char} => 0", end=", ")
        else:
            print(f"{char} => {hash_map[char]}", end=", ")

store_frequency_char("azAxAYzaaaa", ["d", "a", "A", "x", "c", "Y", "z"])