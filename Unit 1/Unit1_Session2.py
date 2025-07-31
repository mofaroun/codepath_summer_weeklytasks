# Unit 1 Session 2 Problems Weekly Tasks

'''
Problem 1

Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.

1. Share 2 questions you would ask to help understand the question:
    What if the list is empty or contains one number?
    What if theyre all the same number?
    
2. Write out in plain English what you want to do: 

    define the function
    create variables for min and max
    return max - min so we dont get negatives
    
3. Translate each sub-problem into pseudocode:
    define max difference(list)
        maximumnum = max of list
        minimumnum = min of list
                
4. Translate the pseudocode into Python and share your final answer:
'''

def max_difference(list):
    if len(list) == 0:
        return 0
    maximumNum = max(list)
    minimumNum = min(list)
    
    return maximumNum - minimumNum


lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

############################################################################################################

'''
Problem 2
Write a function count_less_than() that takes in a list of integers numbers and an integer threshold as parameters and returns the number of items in numbers that are less than threshold

1. Share 2 questions you would ask to help understand the question:
    What if the list is empty?
    
2. Write out in plain English what you want to do: 
    define the function
    create a counter variable set to 0
    check if the length is 0, signifying an empty list
    then iterate through the list
        check if the element at the iteration is less than the threshold
            if it is, we increment counter
    return counter
    
3. Translate each sub-problem into pseudocode:
    def count less than (list, threshold):
        counter = 0 
        if the length of list is 0
            return counter
        
        for every number in the list
            if number is less than threshold
                increment counter
                
4. Translate the pseudocode into Python and share your final answer:
'''

def count_less_than(list, threshold):
    if len(list) == 0:
        return 0
    counter = 0
    for num in list:
        if num < threshold:
            counter += 1
    return counter

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

############################################################################################################

'''
Problem 3
Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.

1. Share 2 questions you would ask to help understand the question:
    What do we return if there are no even numbers?
    What do we do if there are no numbers in the list at all?
    
2. Write out in plain English what you want to do: 
    iterate through every number 
    check if its even
    if it is, add it to a list
    return the list

3. Translate each sub-problem into pseudocode:
    define get events(list)
    if the length of list is 0, return empty list
    create a new list called evens
    for every number in the list
        if the number is even
            append it to the list
    return list
4. Translate the pseudocode into Python and share your final answer:
'''

def get_evens(list):
    if len(list) == 0:
        return []
    
    evens = []
    
    for num in list:
        if num % 2 == 0:
            evens.append(num)
    
    return evens 

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst) # Should return [2, 4]
