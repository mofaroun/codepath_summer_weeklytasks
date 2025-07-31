# Unit 2 Session 2 Weekly Tasks
##################################################################
'''
Problem 1
Write a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.

1. Share 2 questions you would ask to help understand the question:
    What if the candidate doesnt exist in the dictionary?
    What do we return if it exists?
    
2. Write out in plain English what you want to do: 
    Check if the candidate is in the votes dictionary
    if it is, add one to the value (votes)
    if its not, make a new entry and set the value of that key to 1 
    
3. Translate each sub-problem into pseudocode:

    define function (votes, candidate)
    if candidate in votes
        candidate in votes value += 1
    else
        candidate in votes set value to 1
        
4. Translate the pseudocode into Python and share your final answer:
'''

def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

############################################################################################################
'''
Problem 2
Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys

1. Share 2 questions you would ask to help understand the question:
    How do we get a key from a dictionary and compare it to other elements?
    What do we do if one of the dictionarys is empty?
    
2. Write out in plain English what you want to do: 
    make a new list
    for every key in the first dciontary
        if the key is in the second dictionary
            append that eky to the new list      
    return the new list
    
3. Translate each sub-problem into pseudocode:

    define function
    list = []
    for key in dict1
        if key in dict2
            newlist append key
    return list
    
4. Translate the pseudocode into Python and share your final answer:

'''

def common_keys(dict1, dict2):
    newList = []
    for key in dict1:
        if key in dict2:
            newList.append(key)
    return newList
        

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

############################################################################################################
'''
Problem 3

1. Share 2 questions you would ask to help understand the question:
    How can we check if a task's value is the largest in the dictionary?
    How do we delete a entry from a dictionary>
    
2. Write out in plain English what you want to do: 
    create two variables that store the name and the value of a task
    for every task in the dictionary
        if the tasks priority is greater than the value of that variables,
            then we store in respective variables
    delete the stored task from the dictionary
    return the name of the task
    
3. Translate each sub-problem into pseudocode:
    define function (tasks):
        maxtaskname = none
        maxtaskvalue = 0
        
        for every task in tasks
            if tasks [task] > maxtaskvalue
                maxtaskname = task
                maxtaskvalue = tasks[task]
                
        tasks pop (maxtaskname)
        return maxtaskname
4. Translate the pseudocode into Python and share your final answer:

'''
def get_highest_priority_task(tasks):
    maxTaskName = None
    maxTaskValue = 0
    
    for task in tasks:
        if tasks[task] > maxTaskValue:
            maxTaskName = task
            maxTaskValue = tasks[task]
            
    tasks.pop(maxTaskName)
    return maxTaskName        
        

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
