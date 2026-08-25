from collections import defaultdict
class HashTable():
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0 # initialize hash value
        for letter in key:
            my_hash = ((my_hash +ord(letter) * 23) % len(self.data_map))
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])): # linear search through the bucket
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
def item_in_common(list1, list2):
    dic = {}
    for item in list1:
        dic[item] = True # add each item in list 1 to the dictionary
    for item in list2:
        if item in dic: # check if each item in list 2 is in the dictionary
            return True
    return False

def find_duplicate(nums):
    duplicate_list = []
    dic = {}
    for item in nums:
        if item not in dic:
            dic[item] = True # add to dic
        elif item not in duplicate_list: # if item is in dictionary and not in duplicate_list. Note: these if and elif statements already cover all cases
            duplicate_list.append(item)
    return duplicate_list

def first_non_repeating_char(string):
    # handle edge case: empty string
    if len(string) == 0:
        return None 
    
    #scan and add to dictionary(letter:frequency)
    dic = {}
    for letter in string:
        if letter not in dic: # letter not in dic
            dic[letter] = 1
        else: # letter is in dic
            dic[letter] += 1
    # scan through the dic to find the first key which has the freq value == 1
    first = None
    for key in dic.keys():
        if dic[key] == 1:
            first = key
            break
    return first

def group_anagrams(strings):
    if len(strings) == 0: #edge case: no input string
        return None
    
    result = defaultdict(list) # avoid edge case by giving default value
    for string in strings:
        count = [0] * 26 # the problem's constraint is the lowercase English characters
        for char in string:
            count[ord(char) - ord("a")] += 1
        result[tuple(count)].append(string) # list is unhashable, so cast to tuple(immutable)
    return result.values()

def two_sum(nums: list[int], target: int):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [i, seen[complement]]
        seen[num] = i
    return []

if __name__ == "__main__":
    # my_hash_table = HashTable(7)
    # my_hash_table.set_item("bolts", 1400)
    # my_hash_table.set_item("washers", 1200)
    # my_hash_table.set_item("lumber", 70)
    print ( two_sum([3, 3], 6) )