"""
1. Recursion 
- if the input is empty, return an empty array
- initialize a data structure(hash map) that maps digits to their letters, i.e. 6 : ['m', 'n','o']
- use a backtracking function to generate all possible combiantions
    - the function should take 2 primary inputs; the current combination of letters we have,
      path, and index we are current checking
    - As a base case, if our current combination of letters is the same length as the input "digits",
      that manes we have a complete combination. Therefore, add it to our answers, and backtrack
    - otherwise, get all the letters that correspond with the current digit we are looking at, "digits[index]
    - loop through these letters. For each letter, add the letter to our current path, and call backtrack
      again, but move on to the next digit by incrementing "index" by 1
    - make sure to remove the letter from "path" once finished with it 
"""


def letterCombinations(digits):
    # if the input is empty, immediately return an empty answer array
    if len(digits) == 0:
        return []

    # map all the digits to their corresponding letters
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(index, path):
        # if the path is the same length as digits, we have a complete combination
        if len(path) == len(digits):
            combinations.append("".join(path))
            return  # backtrack

        # get the letters that the current digit maps to, and loop through them
        possible_letters = letters[digits[index]]
        for letter in possible_letters:
            # add the letter to our current path
            path.append(letter)
            # move on to the next digit
            backtrack(index + 1, path)
            # backtrack by removing the letter before moving onto the next
            path.pop()

    # initiate backtracking with an empty path and starting index of 0
    combinations = []
    backtrack(0, [])
    return combinations


print(letterCombinations("23"))
