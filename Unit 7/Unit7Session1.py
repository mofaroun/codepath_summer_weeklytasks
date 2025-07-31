'''
Problem 1

Given a sorted list of integers and a value x, return the index of the floor of x. The floor of x is the largest element in the array smaller than or equal to x. If there is no floor of x, return -1.

1. Share 2 questions you would ask to help understand the question:
    What if there is no number smaller than X?
    What is the relationship between the index and what number we return?
    
2. Write out in plain English what you want to do: 
    Since the list is sorted, we can just return i until the element at index i is greater than x
    
3. Translate each sub-problem into pseudocode:

    for i in range length of list
        if list at i > x
            return i - 1 
    
4. Translate the pseudocode into Python and share your final answer:

'''

def find_floor(lst, x):
    
    for i in range(len(lst) - 1):
        if lst[i] > x:
            return i - 1
        
print(find_floor([1, 2, 8, 10, 11, 12, 19], 5))

############################################################################################################
'''

Problem 2

Problem 2: Factorial Cases

Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n. The factorial of a number is the product of all numbers between 1 and n.

Base Case: The smallest number we can find a factorial of is 0. By definition, the factorial of 0 is 1.

Recursive Case: We can restate the problem to say that the factorial of n is n * the factorial of n-1.

1. Share 2 questions you would ask to help understand the question:
    What is the base case?
    What should the return call be?
    
2. Write out in plain English what you want to do: 
    Base case is if n == 1, return 1
    else return n times facotirla n - 1
    
3. Translate each sub-problem into pseudocode:
    if n == 1
        return 1
    return n * factorial(n - 1)
    
4. Translate the pseudocode into Python and share your final answer:

'''
def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
    


############################################################################################################
'''
Problem 3

Without using the built-in sum() function, write a function sum_list() that calculates the sum of all values in a list recursively.

What is the time complexity of this function? What is the space complexity?

1. Share 2 questions you would ask to help understand the question:
    What should the base case be?
    What if the list is empty?
    
2. Write out in plain English what you want to do: 
    If the list is empty, that is our base case
        return 0
    else we return the first element + recursive call sum_list where the parameter is the rest of the list but the first
    
3. Translate each sub-problem into pseudocode:

    if lst == []:
        return 0
        
    return lst[0] + sum_list(lst[1:])
    
4. Translate the pseudocode into Python and share your final answer:

'''

def sum_list(lst):
    if lst == []:
        return 0
    
    return lst[0] + sum_list(lst[1:len(lst)])

print(sum_list([1,2,3,4,5]))
