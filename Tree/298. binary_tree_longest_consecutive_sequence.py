class Solution:
    def __init__(self):
        self.maxLength = 0

    def longestConsecutive(self, root):
        if root is None:
            return 0

        # start from the root node
        self.pathFrom(root, 0, root.val)
        return self.maxLength

    def pathFrom(self, root, length, num):
        if root is None:
            return
        # if current node = previous  node + 1
        if root.val == num + 1:
            # it's consecutive, length + 1
            length += 1
        # else, it's not reset length to 1
        else:
            length = 1

        if length > self.maxLength:
            self.maxLength = length

        self.pathFrom(root.left, length, root.val)
        self.pathFrom(root.right, length, root.val)