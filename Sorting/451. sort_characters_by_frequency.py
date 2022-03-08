"""
1. Hashmap and sort
 - use hashmap to count how many times each character occurs in the string; The key are characters, the value are the number of occurrences
 - next extract a copy of the keys from the hashmap and sort them by frequency using a comparator that looks at the hashmap values 
   to make its decisions
 - finally, initialize a new stringBuilder and then iterate over the list of sorted characters(sorted by frequency), look up the 
   the values in the Hashmap to know how many of each character to append to the stringBuilder
"""


import collections


def frequencySort(s):
    # count up the occurances
    counts = collections.Counter(s)
    # build up the string builder
    string_builder = []
    for letter, freq in counts.most_common():
        # letter * freq make freq copies of letter
        # i.e. 'a' * 3 = 'aaa'
        string_builder.append(letter * freq)

    return "".join(string_builder)


"""
2. Bucket sort
"""


# def frequencySort(s):
#     if not s:
#         return s

#     # determine the frequncy of each character
#     counts = collections.Counter(s)
#     max_freq = max(counts.values())

#     # bucket sort the character by frequency
#     buckets = [[] for _ in range(max_freq + 1)]
#     for char, freq in counts.items():
#         buckets[freq].append(char)

#     # build up the string builder
#     string_builder = []
#     for i in range(len(buckets) - 1, -1, -1):
#         for char in buckets[i]:
#             string_builder.append(char * i)
#     return "".join(string_builder)