"""
Define a recursive function : backtrack(remain, comb, start)
- current combination(comb), remain sum(remain), current cursor(start)

1. Base case
- remain == 0: found the match, add current comb to the final list
- remain < 0: exceed the target value
2. continue to explore [start ... n]
    - add current candidate into the combination
    - with the added candidate, we have less sum to fulfill: remian - candidate
    - for the next candidate, start from the curson start
    - backtrck by poping at the end
"""


def combinationSum(candidates, target):
    results = []

    def backtrack(remain, comb, start):
        if remain == 0:
            results.append(list(comb))  # deep copy, append(comb) -> shallow copy
            return

        if remain < 0:
            return

        for i in range(start, len(candidates)):
            # add the number into the combination
            comb.append(candidates[i])
            # give the current number another chance, rather than moving on
            backtrack(remain - candidates[i], comb, i)
            # backtrack, remove the number from the combination
            comb.pop()

    backtrack(target, [], 0)
    return results


print(combinationSum([2, 3, 6, 7], 7))