def pathSum(root, targetSum):

    allPaths = []
    find_paths_recursive(root, targetSum, [], allPaths)
    return allPaths


def find_paths_recursive(currentNode, targetSum, currentPath, allPaths):
    if currentNode is None:
        return allPaths

    # add the current node to the path
    currentPath.append(currentNode.val)
    # if the current node is a leaf and its value
    # is equal to targetSum, save the current path
    if (
        currentNode.val == targetSum
        and currentNode.left is None
        and currentNode.right is None
    ):
        allPaths.append(list(currentPath))
    else:
        # traverse the left sub-tree
        find_paths_recursive(
            currentNode.left, targetSum - currentNode.val, currentPath, allPaths
        )
        # traverse the right sub-tree
        find_paths_recursive(
            currentNode.right, targetSum - currentNode.val, currentPath, allPaths
        )
    # remove the current node from the path to backtrack
    # we neet to remove the current node while we are going up the recursive call stack
    del currentPath[-1]
