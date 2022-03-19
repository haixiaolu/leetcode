"""
1. Backtracking
    The idea is that we pick the numbers one by one. 
    For a permutation of length N, we would need N stages to generate a valid permutation. 
    - At each stage, we need to pick one number into the permutation, out of the remaining available numbers
    - Later at the same stage, we will try out all availabel choices
    - By trying out, we progressively build up candidates to the solution, and revert each choice
      with another alternative until there is no more choice
    In order to find out all the unique numbers at each stage, we can build a hashtable, with 
    each unique number as the key and its occurrence as the corresponding value
"""
from collections import Counter


def permuteUnique(nums):
    results = []

    def backtrack(comb, counter):
        if len(comb) == len(nums):
            # make a deep copy of the resulting permutation
            # since the permutation would be backtracked later
            results.append(list(comb))
            return

        for num in counter:
            if counter[num] > 0:
                # add this number into the current combination
                comb.append(num)
                counter[num] -= 1
                # continue the exploration
                backtrack(comb, counter)
                # revert the choice for the next exploration
                comb.pop()
                counter[num] += 1

    backtrack([], Counter[nums])
    return results
