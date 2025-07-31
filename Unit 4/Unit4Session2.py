# Unit 4 Session 2 
'''
Problem 1

1. Share 2 questions you would ask to help understand the question:
    How many loops happens? 
    How many checks?
2. Write out in plain English what you want to do: 
    See how many loops and what kind of checks it makes
3. Translate each sub-problem into pseudocode:
    not applicable
4. Translate the pseudocode into Python and share your final answer:
def get_element_at_index(lst, index):
    if index < 0 or index >= len(lst):
        return None  # Handle out-of-bounds cases
    return lst[index]
    
    the Big O of this code is constant big o of 1, O(1) - this is because we're just checking if a value is greater than the length of the list or less than 0 without iterating or traversing.
'''

############################################################################################################
'''
Problem 2

1. Share 2 questions you would ask to help understand the question:
    How many loops happens? 
    How many checks?
2. Write out in plain English what you want to do: 
    Check how many loops or what kind of accesses are happening
3. Translate each sub-problem into pseudocode:
    Not applicable
4. Translate the pseudocode into Python and share your final answer:

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
    
the big o of this code is big o of n, O(n), this is because we are iterating through every num in arr, where n is the length of the array. 
'''

