'''
Problem 1

Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. A uniform substring consists of a single repeated character.

1. Share 2 questions you would ask to help understand the question:
    What is the string is empty?
    What if theyre all the same character?
    
2. Write out in plain English what you want to do: 
    Return the size of a substring where the substring contains all the same characters
3. Translate each sub-problem into pseudocode:
    define the function
    counter = 1
    lengthCheck = 1
    
    for i in range length of string - 1
        if s[i] == s[i+1]:
            lengthcheck += 1
            
        else
            if lengthCheck if create than cmax
                max = lengthcheck
            lengthcheck = 0
            
    return max(counter, lengthchecker)
    
4. Translate the pseudocode into Python and share your final answer:

'''


def longest_uniform_substring(s):

    counter = 1
    lengthCheck = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            lengthCheck += 1
        else:
            if lengthCheck > counter:
                counter = lengthCheck
            lengthCheck = 1

    return max(counter, lengthCheck)


s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)
############################################################################################################
'''

Problem 2

Write a function wordPattern() that takes in a string pattern and a string s as parameters. The function returns True if s follows the pattern and False otherwise. The string follows the pattern if there is a 1:1 correspondence between a letter in the pattern and a non-empty word in s.

1. Share 2 questions you would ask to help understand the question:
    What if the size of S and pattern are different?
    What if S is empty?
    
2. Write out in plain English what you want to do: 
    Create a list to put each word in string s in that list, seperated by spaces
    then make 2 dictionaries, one where the character in pattern is the key and word is the value, and the other where each word is the key with pattern value
    add to the respective dictionarieds if they dont exist, and if they do, check if the values and keys match, else return False
    
3. Translate each sub-problem into pseudocode:
    define the function
    create a word list
    word = ""
    for every character in s:
        add character to word if " " else word = "" and append to word list
    add word to wordList to account for the last word
    
    wordDict = {}
    patternDict = {}
    
    for i in range(len(pattern)):
        p = pattern[i]
    w = wordList[i]
    
    if p in patterndict
        if patterndict[p] != w
            return False
    else
        patterndict[p] = w
        
    if w in worddict
        if worddict[w] != p:
            return false
    
    else
        word dict[w] = p


    return true
                
4. Translate the pseudocode into Python and share your final answer:
'''


def wordPattern(pattern, s):
    # adding s words to list

    wordList = []
    word = ""
    for char in s:
        if char == ' ':
            wordList.append(word)
            word = ""
        else:
            word += char

    wordList.append(word)

    wordDict = {}
    patternDict = {}

    for i in range(len(pattern)):
        p = pattern[i]
    w = wordList[i]

    if p in patternDict:
        if patternDict[p] != w:
            return False
    else:
        patternDict[p] = w

    if w in wordDict:
        if wordDict[w] != p:
            return False
    else:
        wordDict[w] = p
    
    return True

    print(wordDict)
    print(patternDict)


pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
s2 = "dog cat cat fish"
print(wordPattern(pattern, s2))

pattern2 = "aaaa"
s3 = "dog cat dog cat"
print(wordPattern(pattern2, s3))
s4 = "dog dog dog dog"
print(wordPattern(pattern2, s4))
############################################################################################################
'''
Problem 3

Write a function interleave_lists() that accepts two lists as parameters. The function should return a new list that combines the given lists by alternating which list it takes its next element from. It will take elements in order, and if one list is longer it will append the remaining elements to the end of the interleaved list.

1. Share 2 questions you would ask to help understand the question:
    What if both lists are empty?
    What if the length of the lists vary?
    
2. Write out in plain English what you want to do: 
    I want to create a new list, and iterate with a for loop based on the smalled length list
    Once we alternative add to a new list, add the rest of the longer list to the end of the new list
    return new list
    
3. Translate each sub-problem into pseudocode:
    define function
    create new list = 0
    declare index1 = 0
    declare index2 = 0
    
    for i in range(the minumum between length of list 1 or list 2):
        add element at index index1 of list1 to newList
        increment index1
        add element ad index index2 of list 2 to new list
        incrememtn index2
        
    if length of list2 is greater than list 1
        newList = newList + lst2[index2:]
    else
        newList = newList + lst1[index1:]
        
        
4. Translate the pseudocode into Python and share your final answer:

'''

def interleave_lists(lst1, lst2):
    newList = []
    
    index1 = 0
    index2 = 0
        
    for i in range(min(len(lst1), len(lst2))):
        newList.append(lst1[index1])
        index1+=1
        newList.append(lst2[index2])
        index2+=1

    if len(lst2) > len(lst1):
        newList = newList + lst2[index2:]
    else:
        newList = newList + lst1[index1:]
    
    return newList

lst1 = [1, 2, 3, 4]
lst2 = [10, 20]
inter_lst = interleave_lists(lst1, lst2)
print(inter_lst)