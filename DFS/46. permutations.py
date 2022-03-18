def permute(nums):
    results = []

    def backtrack(first):
        # if all integers are used up
        if first == n:
            results.append(nums[:])

        for i in range(first, n):
            # place ith integer first in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutation
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    backtrack(0)
    return results


print(permute([1, 2, 3]))