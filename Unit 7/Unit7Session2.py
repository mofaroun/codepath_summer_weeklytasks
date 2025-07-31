'''
Problem 1

Given a sorted list of integers containing only 0s and 1s, count the total number of 1’s in the array in O(log n) time.

1. Share 2 questions you would ask to help understand the question:
    What is the array has all 0s or 1s?
    What is Log n?
    
2. Write out in plain English what you want to do: 
    Use a binary search algorithm to figure out the last 0 location, and update counter to middle as we iterate
    
3. Translate each sub-problem into pseudocode:

    left = 0
    right = len(lst) - 1
    
    while left < right:
        middle = left + right / 2
        
        if middle lst == 0 
            left = middle + 1
            counter = middle
        elif lst[middle] == 1
            right = middle - 2
        
    return counter +1
    
4. Translate the pseudocode into Python and share your final answer:

'''


def count_zeros(lst):
    left = 0
    right = len(lst) - 1
    counter = -1
    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == 0:
            left = middle + 1
            counter = middle
        elif lst[middle] == 1:
            right = middle - 1

    return counter+1


print(count_zeros([0, 0, 0, 0, 1, 1, 1]))

############################################################################################################
'''
Problem 2

Given two strings s and sub, write a function count_substring() that returns the number of times the substring sub occurs in s. Occurrences should not overlap. A substring is a sequence of adjacent characters within a larger string.

Your solution must be recursive.

Evaluate the time complexity of your solution.

1. Share 2 questions you would ask to help understand the question:
    What is a substring?
    How can we use slicing to our advantage?
    
2. Write out in plain English what you want to do: 
    Use a helper function to see if the first characters up to length of the substring in S is the substring, and recursively call where we cut off the first character in S
    
3. Translate each sub-problem into pseudocode:
    count = 0
    
    def helper(s, sub, count):
        if len s < len sub
            return count
            
        if s[:len sub] == sub:
            count += 1
        
        return helper (s[1:], sub, count)
        
    return helper(s, sub, 0)
    
    
4. Translate the pseudocode into Python and share your final answer:

'''


def count_substring(s, sub):
    count = 0

    def helper(s, sub, count):
        if len(s) < len(sub):
            return count

        if s[:len(sub)] == sub:
            count += 1

        return helper(s[1:], sub, count)

    return helper(s, sub, 0)


print(count_substring("abcdeabcde", "abc"))


############################################################################################################
'''
Problem 3

hus far, we’ve mostly been using an iterative implementation of the binary search algorithm. Recursive implementations of binary search are also very common. Implement binary_search() recursively.

1. Share 2 questions you would ask to help understand the question:
    What if we dont find the target?
    How do we adjust middle?
    
2. Write out in plain English what you want to do: 
    Use binary search with pointers in the functiond definition, repeatedly "cut" the array in half and check middle of new array for target
    
3. Translate each sub-problem into pseudocode:
    if left > right:
        return -1
        
    middle = left + right / 2
    
    if nums[middle] == target:
        return middle
        
    if nums[iddle] < target:
        return binary-search(nums, target, middle, right)
        
    else
        return binary_search(nums, target, left, middle)
        
4. Translate the pseudocode into Python and share your final answer:

'''


def binary_search(nums, target, left, right):

    if left > right:
        return - 1

    middle = (left + right) // 2

    if nums[middle] == target:
        return middle

    if nums[middle] < target:
        return binary_search(nums, target, middle, right)

    else:
        return binary_search(nums, target, left, middle)


nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

print(binary_search(nums, target, 0, len(nums) - 1))
