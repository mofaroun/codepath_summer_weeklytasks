class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
def printNodes(head):
    current = head
    while current:
        print(current.value)
        current = current.next
        
'''
Problem 1

A circular linked list is a linked list where the tail node points at the head node. Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.

Note: a circular list is more than just a cycle - specifically connecting the first and last nodes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

1. Share 2 questions you would ask to help understand the question:
    What makes a circular linked list?
    Where should the check stop?
    
2. Write out in plain English what you want to do: 
    Traverse the list and check to see if the current node is the head -> return true if it is, false if not
    
3. Translate each sub-problem into pseudocode:
    current = head.next
    while current and current != head:
        current = current.next
    
    return current == head
    
4. Translate the pseudocode into Python and share your final answer:

'''

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next= node2
node2.next = node3
node3.next = node4
node4.next = node5

def is_circular(head):
    if not head:
        return False
    
    current = head.next
    
    while current and current != head:
        current = current.next
        
    return current == head

# print(is_circular(node1))

############################################################################################################
'''
Problem 2

Given the head of a linked list and a value val, partition a linked list around val such that all nodes with values less than val come before nodes with values greater than or equal to val.

1. Share 2 questions you would ask to help understand the question:
    How can we keep track of where to place the nodes?
    What do we do when we reach the end of the given list?
    
2. Write out in plain English what you want to do: 
    Create two new linked lists, one for greater than values and one for less than, and 2 pointers that keep track of the ends of these lists
    Traverse through the linked list, and if we come across a node that is greater ahn, add it to the respective list and move its pointer down - do the same with the other
    connect the 2 lists, then return the head of that list.next to get rid of the None at the beginning
    
3. Translate each sub-problem into pseudocode:

    less than = new node(none)
    greaterthan = newnode(none)
    
    lessthan pointer = lessthan
    greaterthanpointer = greaterhan
    
    current = head
    
    while currrent:
        if current value < val
            lessthanpointer.next = node (current value)
            lessthanpointer = lessthanpointer.next
        else
            morethanpter.next = node(current value)
            morethanpointer = morethanpointer.next
            
        current = current.next
        
        lessthanpter.next = morethanpter.next
        
        return lessthan.next
        
4. Translate the pseudocode into Python and share your final answer:

'''


def partition(head, val):
    
    lessThanVal = Node(None)
    moreThanVal = Node(None)
    
    lessThanPter = lessThanVal
    moreThanPter = moreThanVal
    
    current = head
    while current:
        if current.value < val:
            lessThanPter.next = Node(current.value)
            lessThanPter = lessThanPter.next
        else:
            moreThanPter.next = Node(current.value)
            moreThanPter = moreThanPter.next
        current = current.next
        
    lessThanPter.next = moreThanVal.next
    
    return lessThanVal.next


node1 = Node(1)
node2 = Node(4)
node3 = Node(5)
node4 = Node(2)
node5 = Node(5)
node6 = Node(2)

node1.next= node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node7 = Node(1)
node8 = Node(4)
node9= Node(5)
node10 = Node(2)
node11 = Node(5)
node12 = Node(2)

node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12



printNodes(partition(node1, 3))

############################################################################################################
'''
Problem 3

Two linked lists are identical when they have the same values and the same order of values. Given the heads of two linked lists, write a function that returns True if the the linked lists are identical and False otherwise.

1. Share 2 questions you would ask to help understand the question:
    What if theyre different sizes?
    Should we traverse in sync?
    
2. Write out in plain English what you want to do: 
    create two different pointers
    traverse in sync
    if the value at the comparative node pointers are different return false
    return true at the end of the loop
    
3. Translate each sub-problem into pseudocode:
    currant a, current b = heada, headb
    
    while current a and current b:
        if current a value != currentb value:
            return flase
            
        current a = currenta.next
        current b = currenba.next
        
    return true
    
4. Translate the pseudocode into Python and share your final answer:

'''


def is_identical(head_a, head_b):
    current_a = head_a
    current_b = head_b
    
    while current_a and current_b:
        if current_a.value != current_b.value:
            return False
        
        current_a = current_a.next
        current_b = current_b.next
        
    return True

print(is_identical(node1, node7))
