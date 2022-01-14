# method 1, 排序
# def contiansDuplicate(nums):
#     nums.sort()
#     for i in range(len(nums) - 1):
#         if nums[i] == nums[i + 1]:
#             return True
#         else:
#             False


# method 2, hashmap
# def containsDuplicate(nums):
#     hashmap = {}
#     for x in nums:
#         if x not in hashmap:
#             hashmap[x] = 1
#         else:
#             return True
#     return False

# method 3, set
def containsDuplicate(nums):
    return len(nums) != len(set(nums))


obj = containsDuplicate(nums=[1, 2, 3, 2])
print(obj)
