
'''
Problem 1

Given the root of a binary tree, write a function that finds the value of the left most node in the tree.

1. Share 2 questions you would ask to help understand the question:
    How to traverse left?
    What conditions have to be met?
2. Write out in plain English what you want to do: 
    Traverse the tree, stop once we see that root.left is empty
3. Translate each sub-problem into pseudocode:
    if root is none return None
    if root.left is None return root.val
    return recursive call root.left
4. Translate the pseudocode into Python and share your final answer:

'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


headNode = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
headNode2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))


def left_most(root):
    if root is None:
        return None
    if root.left is None:
        return root.val
    return left_most(root.left)


print(left_most(headNode2))


############################################################################################################
'''
Problem 2

Given the root of a binary tree, write a function size() that returns the number of nodes in the binary tree.

1. Share 2 questions you would ask to help understand the question:
    What if root is none?
    How can we traverse the whole tree?
2. Write out in plain English what you want to do: 
    Traverse the tree and everytime we hit a node at a valid root.left or right, recursive call it + 1 to root.left or right
3. Translate each sub-problem into pseudocode:
    if root is none return 0
    return 1 + size(root.left) + size(root.left)
4. Translate the pseudocode into Python and share your final answer:

'''


class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def size(root):
    if root is None:
        return 0
    return 1 + size(root.right) + size(root.left)


print(size(headNode))


############################################################################################################
'''
Problem 3

Given a value and the root of a binary search tree, write a function find_bst() that returns True if there is a node with the given value in the tree. Assume the tree is balanced.

1. Share 2 questions you would ask to help understand the question:
    What if root is None?
    WHat if we dont find the right value?
2. Write out in plain English what you want to do: 
    base case, root.val == value then return true, if root is None we return false - we dont find the value we're looking for
3. Translate each sub-problem into pseudocode:
    if root is None: return False
    if root val == valu return true
    if value < root val 
        recursve call root.left
    else recursive call root.right

4. Translate the pseudocode into Python and share your final answer:

'''


def find_bst(root, value):
    if root is None:
        return False
    if root.val == value:
        return True

    if value < root.val:
        return find_bst(root.left, value)

    return find_bst(root.left, value)


print(find_bst(headNode2, 25))
