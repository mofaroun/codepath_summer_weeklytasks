# Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.

def is_subsequence(lst, sequence):
    index = 1
    sequence[index] = 6, 1
    
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [6, 1, -1, 10]
print(is_subsequence(, sequence))