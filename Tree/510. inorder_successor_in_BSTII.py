def inorderSuccessor(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node

    else:
        while node.parent and node.val > node.parent.val:
            node = node.parent
        if node.parent == None:
            return None
        else:
            return node.parent