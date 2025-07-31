# Unit 4 Session 1 

'''
Problem 1

Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

1. Share 2 questions you would ask to help understand the question:
    What is a prime number?
    What number do we check against?
    
2. Write out in plain English what you want to do: 
    Divide n by all the numbers up to itself
    
3. Translate each sub-problem into pseudocode:
    define function
        for i in range 2 , n // 2 + 1
            if n % i == 0
                return false
        return true
        
4. Translate the pseudocode into Python and share your final answer:

'''

def is_prime(n):
    
    for i in range(2, n // 2 + 1):
        if(n % i == 0):
            return False                 
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9)) 

#############################################################################################################
'''
Problem 2
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

1. Share 2 questions you would ask to help understand the question:
    How can we replace elements with eachother?
    Where should we have pointers?
    
2. Write out in plain English what you want to do: 
    create two pointers that point to opposite ends of the list
    create a while loop that replaces the elements at those pointers with eachother
    decrement right incrememnt left and continue
3. Translate each sub-problem into pseudocode:
    define function
        left = 0 
        right = length of list - 1
        
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            decrement right
            increment left
            
        return lst
        
        
4. Translate the pseudocode into Python and share your final answer:

'''

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while right > left:
        lst[left], lst[right] = lst[right], lst[left]
        right-=1
        left +=1 
        
    return lst

print(reverse_list([1,2,3,4,5]))
    
############################################################################################################
'''
Problem 3

Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first palindromic string in the list. A string is palindromic if it reads the same forward and backward. If there is no such string, return an empty string ""

1. Share 2 questions you would ask to help understand the question:
    What is a palindrome?
    How can we access 1 word at a time?
    
2. Write out in plain English what you want to do: 
    use a for loop to iterate through every word
    for every word make 2 pointers that point to opposite ends
        check if the letters are not equal, with a while loop 
        if they are, decrement and incremement
        if theyre not break the while loop and move on to the next word in the for loop
        once right is < left: return true
        
    return ""
3. Translate each sub-problem into pseudocode:
    define function
        for every word in words
            left = 0
            right = length of word - 1
            
            while right > left
                if word[right] != word[right]
                    break
                    
                right -= 1
                left += 1
            else:
                return word
                
        return ""
4. Translate the pseudocode into Python and share your final answer:

'''

def first_palindrome(words):
    
    for word in words:
        left = 0
        right = len(word) - 1

        while right > left:
            if word[left] != word[right]:
                break
            
            right -=1
            left += 1
            
            
        else:
            return word
    
    return ""


                  
        
        
            
    

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)