"""
- Initialize left and right indexes left = 0 and right = m * n - 1
- while left <= right:
    - pick up the index in the middle of the virtual array as a pivot index: mid = (left + right) // 2
    - The index corresponds row = mid // n and column = mid % n in the intial matrix, and hence one could ge the pivot element . 
      This element splits the virtual array in two parts
    - compare pivot element and target to identify in which part one has to look for target    
"""


def searchMatrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    # binary search
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        pivot_element = matrix[mid // n][mid % n]
        if pivot_element == target:
            return True
        else:
            if pivot_element > target:
                right = mid - 1
            else:
                left = mid + 1
    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))