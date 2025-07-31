'''
Problem 1

Write a function remove_char() that takes in a string s and an integer n as parameters, The function returns a new string with the nth character removed where 0 < n < len(s).

1. Share 2 questions you would ask to help understand the question:
    What if its an empty string?
    What if the character isnt in the given string?
    
2. Write out in plain English what you want to do: 
    Create a new string, then iterate and add every character that isnt the character to remove to the new string
    
3. Translate each sub-problem into pseudocode:
    define function
    newString = ""
    for i in range length of s
        if i is n
            continue
        else
            newString += s at i
    return new String
    
4. Translate the pseudocode into Python and share your final answer:

'''

def remove_char(s, n):
    newString = ""
    for i in range(len(s)):
        if i == n:
            continue
        else:
            newString+=s[i]
    
    return newString
# s = "typpo"
# fixed_s = remove_char(s, 2)
# print(fixed_s)

############################################################################################################
'''
Problem 2

Write a function vowel_count() that takes in a string s as a parameter and returns the number of vowels in the given string.

1. Share 2 questions you would ask to help understand the question:
    What if the string is empty?
    Is the given string going to be of varying cases?
    
2. Write out in plain English what you want to do: 
    iterate through the string with a for loop, and turn each character into lowerecase, then checking if its in a list of vowels. If it is, incrememnt number of bowels
    
3. Translate each sub-problem into pseudocode:
    define function
    list of vowels [a,e,i,o,u]
    set numberofvowels to 0
    for each character in s
        lowercase character
        if lowerchase character in vowels
            number of vowels += 1
    return number of vowels
    
4. Translate the pseudocode into Python and share your final answer:

'''

def vowel_count(s):
    vowels = ['a', 'e', 'i','o','u']
    numVowels = 0
    for char in s:
        char = char.lower()
        if char in vowels:
            numVowels += 1
            
    return numVowels

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)
############################################################################################################
'''
Problem 3

Write a function find_the_needle() that takes in two string parameters: a needle and a haystack. The function returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

1. Share 2 questions you would ask to help understand the question:
    What if the needle or haystack are empty strings?
    Can we use buil in python functions?
    
2. Write out in plain English what you want to do: 
    slice the haystack, using i and i + length of needles as the slicing indexes, and use a for loop to iterate through the characters checking if they equal needle
    
3. Translate each sub-problem into pseudocode:
    define the function
    set index = length of needle
    
    for i in range length of haystack
        if haystack[i: i + index] == needle
            return i
            
    return -1 if we dont find needle in haystack
    
4. Translate the pseudocode into Python and share your final answer:

'''

def find_the_needle(haystack, needle):
    index = len(needle)
    
    for i in range(len(haystack)):
        if haystack[i:i+index] == needle:
            return i
        
    return -1

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))