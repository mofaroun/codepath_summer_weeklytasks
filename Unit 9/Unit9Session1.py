
'''
Problem 1

Given the root of a binary tree, return True if the tree’s left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). Return False otherwise.

1. Share 2 questions you would ask to help understand the question:
    
2. Write out in plain English what you want to do: 

3. Translate each sub-problem into pseudocode:

4. Translate the pseudocode into Python and share your final answer:

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    def helper(node_a, node_b):
        if not node_a and not node_b:
            return True
        if node_a and not node_b or node_b and not node_a or node_a.val != node_b.val:
            return False
        return helper(node_a.left, node_b.right) and helper(node_a.right, node_b.left)
    return helper(root.left, root.right)

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(root))

############################################################################################################
'''
Problem 2

Given the root of a binary tree, return a list of all root-to-leaf paths in any order.

1. Share 2 questions you would ask to help understand the question:
    
2. Write out in plain English what you want to do: 

3. Translate each sub-problem into pseudocode:

4. Translate the pseudocode into Python and share your final answer:

'''

def binary_tree_paths(root):
    list = []
    
    def helper(node, list):
        if not node.left or not node.right:
            list.append(node.)
############################################################################################################
'''
Problem 3

1. Share 2 questions you would ask to help understand the question:
    
2. Write out in plain English what you want to do: 

3. Translate each sub-problem into pseudocode:

4. Translate the pseudocode into Python and share your final answer:

'''
