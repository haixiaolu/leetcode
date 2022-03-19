"""
1. backtracking
    - Backtracking function which takes first integer to add and a current combination as 
      argument 'backtrack(first, curr)'
        - if the current combination is done - add it to output
        - iterate over the integers from first to n
            - add integer i into the current combination curr 
            - proceed to add mroe integers into the combination: [backtrack(i + 1, curr)]
            - Backtrack by removing i from curr 
"""


def combine(n, k):
    def backtrack(first=1, curr=[]):
        # if the combination is done
        if len(curr) == k:
            output.append(curr[:])

        for i in range(first, n + 1):
            # add i into the current combination
            curr.append(i)
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()

    output = []
    backtrack()
    return output
