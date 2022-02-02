"""
Given an unsorted array containing numbers and a number 'k', 
find the first 'k' missing positive numbers in the array
"""
"""
Approach:
It shares similarites with 'Find the Smallest Missing Positive Number'
Follow a similar approach:
    - place the number at its correct indices, ignore all numbers that are out of range
    - Once we are done, iterate through the array to find duplicates that do not have the correct number
    - if can't find 'k' missing number, need to add additional numbers to the output array
    - find these additional numbers we will use the length of the array
"""


def find_first_k_missing_positive(nums, k):
    n = len(nums)
    i = 0
    for i in range(n):
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    missingNUmbers = []
    extraNumbers = set()
    for i in range(n):
        if len(missingNUmbers) < k:
            if nums[i] != i + 1:
                missingNUmbers.append(i + 1)
                extraNumbers.add(nums[i])
    # add the remaining missing nubmers
    i = 1
    while len(missingNUmbers) < k:
        candidateNumber = i + n
        # ignore if the array contains the candidate number
        if candidateNumber not in extraNumbers:
            missingNUmbers.append(candidateNumber)
        i += 1

    return missingNUmbers