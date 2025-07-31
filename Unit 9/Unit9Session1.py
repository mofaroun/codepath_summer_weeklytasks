
'''
Problem 1

Given the root of a binary tree, return True if the tree’s left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). Return False otherwise.

1. Share 2 questions you would ask to help understand the question:
    How can we traverse down the left and right sides?
    Do we need a helper function?
    
2. Write out in plain English what you want to do: 
    Create a helper function that goes through the subtrees
    Check if node A and node B dont exist as the base case -> went through the whole tree -> return true
    check if node a exists while node B doesnt and vice verse OR if both nodes exist and they have different values -> return false
    return recursive call
    
3. Translate each sub-problem into pseudocode:

    def isSymm(root):
        helper(a, b):
            if not a and not b:
                return true
            if not a and b, or not b and a, or a.val != b.val:
                return false
            return helper(a.left, b.right) and helper(a.right, b.left)
            
        return helper(root)
        
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


root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(root))

############################################################################################################
'''
Problem 2

Given the root of a binary tree, return a list of all root-to-leaf paths in any order.

1. Share 2 questions you would ask to help understand the question:
    What is a leaf node?
    What should the basecase be?
    
2. Write out in plain English what you want to do: 
    If node is non then we just return
    else we add the root val
    if leaf, we append path to paths
    recursively call down the left and right if respect children exist
    
3. Translate each sub-problem into pseudocode:

    def binary tree(root)
        def helper(node, path, paths);
            path.append node val
            if not node left and not node right:
                paths.append(path.copy)
            if node left -> recursive call down left
            if node right -> recursive call down right
             
4. Translate the pseudocode into Python and share your final answer:

'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_paths(root):
    
    def helper(node, path, paths):
        if node is None:
            return 
                   
        path.append(node.val)
        
        if not node.left and not node.right:
            paths.append(path.copy())
            
        if node.left:
            helper(node.left, path, paths)
        if node.right:
            helper(node.right, path, paths)
        
        path.pop()
        return paths
    
    paths = []
    return helper(root, [], paths)

root = TreeNode(1, TreeNode(2, right = TreeNode(5)), TreeNode(3))

# print(binary_tree_paths(root))


############################################################################################################
'''
Problem 3

Given the root of a binary search tree, return the minimum difference between the values of any two different nodes in the tree.

1. Share 2 questions you would ask to help understand the question:
    How can we traverse all the nodes?
    Are there any negatives to be expected?
    
2. Write out in plain English what you want to do: 
    Go through all the nodes
    Subtract inorder which nodes have the smallest difference
    
3. Translate each sub-problem into pseudocode:
    def min diff(root)
        helper(node, nodes)
            helper(node.left, nodes)
            nodes.append(node.val)
            helper(node.eright, nodes)
            
            return nodes
            
        nodes = helper(root, [])
        
        min diff = max(nodes)
        for i in range 1, len nodes - 1
            min diff = min(min_diff, nodes[i] - nodes[i - 1])
        return min_diff
    
4. Translate the pseudocode into Python and share your final answer:

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_diff_in_bst(root):
    
    def helper(node, nodes):
        if node is None:
            return
        
        helper(node.left, nodes)
        nodes.append(node.val)
        helper(node.right, nodes)
        
        return nodes
        
    nodes = helper(root, [])
    
    min_diff = float('inf')
    for i in range(1, len(nodes) - 1):
        min_diff = min(min_diff, nodes[i] - nodes[i-1])

    return min_diff

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6), )
rootTwo = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
print(min_diff_in_bst(rootTwo))


