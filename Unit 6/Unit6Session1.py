class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


testHead = Node(1, Node(7, Node(3, Node(4, Node(3, Node(2, Node(1)))))))

'''
Problem 1

A variation of the two-pointer technique introduced in Unit 4 is to have a slow and a fast pointer that increment at different rates. Given the head of a linked list, use the slow-fast pointer technique to find the middle node of a linked list. If there are two middle nodes, return the second middle node.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

1. Share 2 questions you would ask to help understand the question:
    Where do the pointers start at?
    How do we traverse the list at different speeds?
    
2. Write out in plain English what you want to do: 
    Create two pointers for slow and fast
    Incremement fast by 2 nodes and slow by 1 node
    By the time fast is broken, Slow is at the middle
    
3. Translate each sub-problem into pseudocode:
    slow, fast = head
    while fast and fast.next
        fast = fast.next.next
        slow = slow.next
    return slow.value
    
4. Translate the pseudocode into Python and share your final answer:

'''


def find_middle_element(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow.value

# The solution is O(n) time where N is the length of linkedlist. It is O(1) space as space is constant and not changing
print(find_middle_element(testHead))


############################################################################################################
'''
Problem 2

Given the head of a linked list, return a dictionary that maps each unique element in the list to its frequency.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

1. Share 2 questions you would ask to help understand the question:
    What is the best way to track frequencies?
    What do we check for?
    
2. Write out in plain English what you want to do: 
    Create a dictionary
    Traverse current throughout the linkedlist
        If current's value in the dictonary, Plus 1 that key
        else, Add that key to the dictionary
    return dictionary
    
3. Translate each sub-problem into pseudocode:
    freqmap = {}
    current = head
    while current
        if current value in freqmap
            freqmap[currentvalue] += 1
        else 
            freqmap[currentvalue] = 1
    return freqmap
    
4. Translate the pseudocode into Python and share your final answer:
'''

def frequency_map(head):
    frequencyMap = {}
    
    current = head
    
    while current:
        if current.value in frequencyMap:
            frequencyMap[current.value] += 1
        else:
            frequencyMap[current.value] = 1

        current = current.next
        
    return frequencyMap

# Time complexity -> O(n) for N is the length of the linkedlist
# Space Complexity -> O(n) where N is worst case scenerio where all linkedlist values are unique
print(frequency_map(testHead))

############################################################################################################
'''
Problem 3

Given the head of a linked list where each node is an integer value, return the maximum value in the linked list.

1. Share 2 questions you would ask to help understand the question:
    How do we compare values of a linked list?
    Where do we start?
    
2. Write out in plain English what you want to do: 
    Set the starting comparison value to head's value
    While current is valid
        if current value is greater than max
            set max to current value
        traverse current
    return max value
    
3. Translate each sub-problem into pseudocode:
    max = head.value
    current = head
    while current:
        if current.value > max
            max = current.value
        current = current next
        
    return max
4. Translate the pseudocode into Python and share your final answer:

'''

def find_max(head):
    max = head.value
    
    current = head
    
    while current:
        if current.value > max:
            max = current.value
        current = current.next
        
    return max

print(find_max(testHead))
