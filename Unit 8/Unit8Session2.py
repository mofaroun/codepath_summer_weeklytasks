
'''
Problem 1

1. Share 2 questions you would ask to help understand the question:
    What if the values dont match?
    How can we check for values at opposite sides?
2. Write out in plain English what you want to do: 
    Traverse the tree, if the root is None we return false
    If we come across any two nodes that arent the same value we return false
    recursive call root.left and root.right
3. Translate each sub-problem into pseudocode:
    if root is none return true
    if root left and root.left != root.val return false
    if root right and root right !+ root val return false
    recursive call root.left AND recursive call root.right
4. Translate the pseudocode into Python and share your final answer:

'''

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_univalued(root):
    if root is None:
        return True
    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False
    return is_univalued(root.left) and is_univalued(root.right)


############################################################################################################
'''
Problem 2

1. Share 2 questions you would ask to help understand the question:
    How can we find the max of the subtrees?
    What is our base case?
2. Write out in plain English what you want to do: 
    Return the max of recursive calls down the left and right subtrees
3. Translate each sub-problem into pseudocode:
    if root is none return 0
    return recursive call 1 + max (height-> left), (height -> right)
4. Translate the pseudocode into Python and share your final answer:

'''

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

############################################################################################################
'''
Problem 3

1. Share 2 questions you would ask to help understand the question:
    What are the properties to keep in a Binary Tree?
    How can we navigate to keep the conditions true?
    
2. Write out in plain English what you want to do: 
    Traverse the tree and navigate left or right depending on the value of the root and our value
    return the node as the basecase
3. Translate each sub-problem into pseudocode:
    if root is none return node, value
    if key < root.key -> recursive call on root.left
    if key > root.key -> recursive call on root.right
    return root
4. Translate the pseudocode into Python and share your final answer:

'''

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right
   
def insert(root, key, value):
    if root is None:
        return TreeNode(key, value)
    
    if key < root.key:
        root.left  = insert(root.left, key, value)
    elif key > root.key:
        root.right = insert(root.right, key, value)
    
    
    return root


############################################################################################################