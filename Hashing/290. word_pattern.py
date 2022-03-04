"""
# HashMap ( 2 hashmap)
- one hashmap for letter to word
- another one is word to letter
"""
from distutils.util import change_root


def wordPattern(pattern, s):
    words = s.split("")
    if len(pattern) != len(words):
        return False

    charToWord = {}
    wordToChar = {}

    for c, w in zip(pattern, words):
        if c in charToWord and charToWord[c] != w:
            return False
        if w in wordToChar and wordToChar[w] != c:
            return False
        charToWord[c] = w
        wordToChar[w] = c
    return True