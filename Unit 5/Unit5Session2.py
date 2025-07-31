class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
  
def print_nodes(head):
    current = head
    while current:
        print(current.value)
        current = current.next

'''
Problem 1

Write a function list_to_linked_list() that takes in a list lst as a parameter and converts it to a linked list. The function should return the head of the linked list.

1. Share 2 questions you would ask to help understand the question:
    What is the logical sequence for creating a node?
    How do we link nodes?
    
2. Write out in plain English what you want to do: 
    Create a dummy node to mark a new linked list
    set a current variable to dummy so we can add things to it
    
    then for every elemnt in the list
    make a new node with that element in the node
    traverse current to the next node
    
3. Translate each sub-problem into pseudocode:

    def list to linked list (list):
        dummy = new node
        current = dummy
        
        for element in list
            current.next = node(element)
            crrent = current.next

        return dummy
        
4. Translate the pseudocode into Python and share your final answer:

'''

def list_to_linked_list(lst):
    
    dummy = Node(None)
    current = dummy

    for element in lst:
        current.next = Node(element)
        current = current.next
        
    return dummy.next




############################################################################################################
'''
Problem 2

Write a function delete_tail() that takes in a head of a linked list as a parameter and removes the tail from the end of the list.

1. Share 2 questions you would ask to help understand the question:
    How do we get to the end of the list?
    What do we do once we get to the end?
    
2. Write out in plain English what you want to do: 
    Go to the node right before te node tahts at the end of the list so we can remove the next pointer and get rid of the last node
    
3. Translate each sub-problem into pseudocode:

    def delete tail(head)
        current = head
        
        while current has 2 nodes after it
            move current one node down
        
        current next = none
        
        return head
        
4. Translate the pseudocode into Python and share your final answer:

'''

def delete_tail(head):
    current = head
    while current.next.next:
        current = current.next
    
    current.next = None
    
    return head

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]

headTest = list_to_linked_list(normal_list)

print_nodes(headTest)
delete_tail(headTest)
print()
print_nodes(headTest)
        

############################################################################################################
'''
Problem 3

The function should remove the first node it finds in the linked list with value val and return the head of the linked list. If no node can be found with the value val, return the list unchanged.

1. Share 2 questions you would ask to help understand the question:
    How do we check for which node to remove?
    How do we make sure we dont get rid of nodes without affecting the other nodes
    
2. Write out in plain English what you want to do: 

    check if the value of the node we're at is the value
        if it is, we move current.next to current.next.next to ignroe the node that has the value we want to dlete
    else
        we move current.next= current.next.next
        
3. Translate each sub-problem into pseudocode:
    current = head
    while current.next
        if current.next and current.next.value == val
            current.next = current.next.next
        else
            current = current.next
    return head
    
4. Translate the pseudocode into Python and share your final answer:

'''

def ll_remove(head, val):
    current = head
    
    while current.next:
        if current.next and current.next.value == val:
            current.next = current.next.next
        else:
            current = current.next
    return head
