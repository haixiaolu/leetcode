"""
Question: Given a string s consisting of some words separated by some number of spaces,
          return the length of the last word in the string 

          A word is a maximal substring consisting of non-spacing characters only

Input: s = "Hello World"  Output: 5  Explanation: the last word is 'World" with a length of 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        for i in x[::-1]:
            if i != "":
                return len(i)
        return 0
