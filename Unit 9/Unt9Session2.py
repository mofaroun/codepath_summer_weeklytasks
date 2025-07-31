
'''
Problem 1

Given the following pseudocode and the root of a binary tree, return a list of the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).

1. Share 2 questions you would ask to help understand the question:
    What is the tree is empty?
    What is level order?
    
2. Write out in plain English what you want to do: 
    Go through the binary tree in a lever order
        
3. Translate each sub-problem into pseudocode:
    if root is none
        return []
        
    queue = dequeue
    list = []
    
    add root to queue
    while queue
        popped node - node.left
        list.append popped node
        
        if left -> poppednode.left
        if right -> poppednode.right
        
    
4. Translate the pseudocode into Python and share your final answer:

'''

from collections import deque  # This is a popular library used for queues
from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def level_order(root):
    # If the tree is empty:
    if root is None:

        # return an empty list
        return []

    # Create an empty queue using deque
    queue = deque()
    # Create an empty list to store the explored nodes
    list = []

    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    while queue:

        # Pop the next node off the queue (pop from the left side!)
        poppedNode = queue.popleft()

    # Add the popped node to the list of explored nodes
        list.append(poppedNode.val)

    # Add each of the popped node's children to the end of the queue
        if poppedNode.left:
            queue.append(poppedNode.left)
        if poppedNode.right:
            queue.append(poppedNode.right)

    # Return the list of visited nodes
    return list


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6), )
# print(level_order(root))

############################################################################################################
'''
Problem 2

Given the root of a binary tree, return its minimum depth. The minimum depth is the number of nodes along the shortest path from the root down to the nearest leaf node.

Evaluate the time complexity of your solution. Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

1. Share 2 questions you would ask to help understand the question:
    What if node is none?
    What do we do when we come aceoss a leaf node?
    
2. Write out in plain English what you want to do: 
    traverse the tree, for every recursive call add 1, until we hit a leaf node in which we return
3. Translate each sub-problem into pseudocode:

4. Translate the pseudocode into Python and share your final answer:

'''


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def min_depth(root):

    def helper(node):
        if node is None:
            return 0
        
        if not node.left and not node.right:
            return 1 + min(helper(node.right), helper(node.right))
        if node.left and node.right:
            return 1 + helper(node.left)
        if node.right:
            return 1 + helper(node.right)
    return helper(root)
        


rootTwo = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(min_depth(rootTwo))

############################################################################################################
'''
Problem 3

1. Share 2 questions you would ask to help understand the question:
    
2. Write out in plain English what you want to do: 

3. Translate each sub-problem into pseudocode:

4. Translate the pseudocode into Python and share your final answer:

'''


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def print_by_level(root):
    # If the tree is empty:
    if root is None:

        # return
        return

    # Create an empty queue using deque
    queue = deque()

    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    while queue:

        # Pop the next node off the queue (pop from the left side!)
        poppedNode = queue.popleft()

    # Print the popped node
        print(poppedNode.val)

    # Add each of the popped node's children to the end of the queue
        if poppedNode.left:
            queue.append(poppedNode.left)
        if poppedNode.right:
            queue.append(poppedNode.right)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6), )
# print_by_level(root)
