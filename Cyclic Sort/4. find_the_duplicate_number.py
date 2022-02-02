# leetcode 287. Find the Duplicate Number
"""
Given an unsorted array containing n + 1 number taken from the range 1 to n.
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. 
"""
"""
Approach:
It shares similarities with "Find the Missing Number"
- try to place each number on its correct indices. 
- Since there is only one duplicate:
-- if while swapping the number with its index both the numbers being swapped are same, we have found our duplicates
"""


def findDuplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                return nums[i]
        else:
            i += 1

    return -1


def main():
    print(findDuplicate([1, 2, 4, 4]))


main()

# Follow up
"""Can we do this in O(1) space, without modifyiny the input array"""
"""
Approach:
- while doing the cycle sort, we realized that the array will have a cycle due to the duplicate number
  and that the start of the cycle will always point to the duplicate number. 
- This means that we can use the Fast & Slow pointer method to find the duplicate number or the start of the 
  cycle similar to 'Start of LinkedList Cycle'
"""


def find_duplicate(arr):
    slow, fast = arr[0], arr[arr[0]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    # find cycle length
    current = arr[arr[slow]]
    cycleLength = 1
    while current != arr[slow]:
        current = arr[current]
        cycleLength += 1
    return find_start(arr, cycleLength)


def find_start(arr, cycleLength):
    pointer1, pointer2 = arr[0], arr[0]
    # move pointer2 ahead 'cycleLength' steps
    while cycleLength > 0:
        pointer2 = arr[pointer2]
        cycleLength -= 1

    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = arr[pointer1]
        pointer2 = arr[pointer2]

    return pointer1


# def main():
#     print(find_duplicate([1, 4, 4, 3, 2]))
#     print(find_duplicate([2, 1, 3, 3, 5, 4]))


# main()