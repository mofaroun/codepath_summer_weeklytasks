# Unit 2 Session 2 Weekly Tasks
############################################################################################################

'''
Problem 1

Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.

1. Share 2 questions you would ask to help understand the question:
    What if the sequence is empty, what should it return?
    What if the sequence is all of the same number?
    
2. Write out in plain English what you want to do: 
    check if every number exists in the list, but make sure that the order of the sequence is kept throughout the list
    
3. Translate each sub-problem into pseudocode:

    define the function
        create an index variable
        create a for loop for every number in the list
            for every number in the original list if the number is the same as the number at index index, then we incrememtn index
        return true if index is the same size as sequence and false if it isnt
4. Translate the pseudocode into Python and share your final answer:
'''
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6]

def is_subsequence(lst, sequence):
    index = 0
    
    for num in lst:
        if index == len(sequence):
            return True
        
        if sequence[index] == num:
            index += 1
    
    return False

print(is_subsequence(lst, sequence))

############################################################################################################
'''
Problem 2

Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.

keys[i] should be paired with values[i] in the dictionary where 0 <= i <= len(keys). You may assume keys and values are the same length.

1. Share 2 questions you would ask to help understand the question:
    What if the lists are empty, what should we return?
    Which keys belong to which values?
    
2. Write out in plain English what you want to do: 
    Create a new dictionary where the value of values at index i, its key is the value at index i of keys
    
3. Translate each sub-problem into pseudocode:
    new dict = {}
    for i in range of keys
        newDict keys at i = values at i
    return newDict
    
4. Translate the pseudocode into Python and share your final answer:
'''

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]

def create_dictionary(keys, values):
    newDict = {}
    for i in range(len(keys)):
        newDict[keys[i]] = values[i]
    return newDict
        

print(create_dictionary(keys, values))

############################################################################################################
'''
Problem 3
Write a function print_pair() that takes in a dictionary dictionary and a key target as parameters. The function looks for the target and when found, it prints the key and it's associated value as "Key: <key>" followed by "Value: <value>". If target is not in dictionary, print "That pair does not exist!".

1. Share 2 questions you would ask to help understand the question:
    How do we check if a key is in the dictionary?
    What do we return when we find the key if it exists?
    
2. Write out in plain English what you want to do: 
    Check if the key is in the dictionary
    if it is, print out the key and the value
    if it isnt, print out that its not in the ditionary
    
3. Translate each sub-problem into pseudocode:

    define function(target, dictionary)
        if target in dictionary
            print target + dictionary[target]
        else
            print("target not in dictionary)
    
4. Translate the pseudocode into Python and share your final answer:
'''

def print_pair(dictionary, target):
    if target in dictionary:
        print("Key: " + target)
        print("Value: " + dictionary[target])
    else:
        print("That pair does not exist!")
        
dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
############################################################################################################
