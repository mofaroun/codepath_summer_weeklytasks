'''
Problem 1

Update the Pokemon class with a new method catch() that takes in no parameters except self.

The method should update the Pokemon's is_caught attribute to True and not return any value.

1. Share 2 questions you would ask to help understand the question:
    How can we access an object?
    Do all objects have the same attributes?
    
2. Write out in plain English what you want to do: 
    Create a function with a self parameter
    Define it by changing that self's objects attribute to is_caught = true
    
3. Translate each sub-problem into pseudocode:
    def catch(self):
        self.is_caught = true
        
4. Translate the pseudocode into Python and share your final answer:

'''


class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def catch(self):
        self.is_caught = True


############################################################################################################
'''
Problem 2

Update the Pokemon class with a new method choose() that takes in no parameters except self.

If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".

Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!".

1. Share 2 questions you would ask to help understand the question:
    Is self always gonna be a pokemon object?
    What do you return depending on every situation?
    
2. Write out in plain English what you want to do: 
    Define the function
    Check if is caught is true, if it is then print I choose you
    If its not, print is wild catch them if you can
    
3. Translate each sub-problem into pseudocode:
    def choose(self):
    if self is caught == true
        print i choose you
    esle
        print pokemon is wild catch them if you can
        
4. Translate the pseudocode into Python and share your final answer:

'''


class Pokemon:

    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types,  # Output: "types": ["Water"],
            "is_caught": self.is_caught  # Output: "is_caught": False
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if (self.is_caught):
            print(self.name, "I choose you!")
        else:
            print(self.name, "is wild! Catch them if you can")



############################################################################################################
'''
Problem 3

Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

It should add new_type to the Pokemon's list of types.

1. Share 2 questions you would ask to help understand the question:
    How we can access  the types list?
    How do we access the objects own types list?
    
2. Write out in plain English what you want to do: 
    Access the self's types attribute, and then append as you would with a regular list
    
3. Translate each sub-problem into pseudocode:
    def add type(self, new type):
        self.types.append(new_type)
        
4. Translate the pseudocode into Python and share your final answer:

'''

############################################################################################################

class Pokemon:

    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types,  # Output: "types": ["Water"],
            "is_caught": self.is_caught  # Output: "is_caught": False
        })

    def catch(self):
        self.is_caught = True

    def choose(self):
        if (self.is_caught):
            print(self.name, "I choose you!")
        else:
            print(self.name, "is wild! Catch them if you can")
    
    def add_type(self, new_type):
        self.types.append(new_type)
        


