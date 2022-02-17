from numpy import r_


def longestConsecutive(root):
    def helper(node, parent):
        nonlocal max_length
        if not node:
            return 0, 0  # increasing, decreasing
        l_inc, l_dec = helper(node.left, node)
        r_inc, r_dec = helper(node.right, node)
        max_length = max(max_length, l_inc + r_dec + 1, l_dec + r_dec + 1)
        # TODO
        if parent and node.val + 1 == parent.val:
            return max(l_inc, r_inc) + 1, 0
        elif parent and node.val - 1 == parent.val:
            return 0, max(l_dec, r_dec) + 1
        return 0, 0

    max_length = 0
    helper(root, node)
    return max_length