"""
# Compare adjacent words
compare each pair of adjacent words to see if they are sorted exicographically
- Algorithm:
    - Initialize a hashmap to reocrd the relations between each letter and its ranking in order
    - iterate over words and compare each pair of adjacent words
        - iterate over each letter to find the first differnet letter between words[i] and words[i + 1]
        - if words[i + 1] ends before words[i] and no differnt letters are found, then we need to return
          False (apple and app example)
        - if we find the first different letter and the two words are in the correct order, then we can exist
          from the current iteration and proceed to the next pair of words
        - if we find the first different letter and the two words are in the wrong order, then False
"""


def isAlienSorted(words, order):
    order_map = {}
    for index, val in enumerate(order):
        order_map[val] = index

    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            # if we dont find a mismatch letter between words[i] and words[i + 1]
            # we need to examine the case when words are like
            if j >= len(words[i + 1]):
                return False

            if words[i][j] != words[i + 1][j]:
                if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                    return False
                # if we find the first different character and they are sorted
                # then there's no need to check remaining letters
                break
    return True
