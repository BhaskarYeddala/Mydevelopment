"""
Decorators in python
-------------------------
Prerequisites for Decorators
-------------------------
In python everything is treated as an object
Funcation aliasing --> giving another reference name
Nested Functions --> A function inside another funcation
Funcation as an retrun value --> Funcation can return another funcation
Funcation as a Argument --> Funcation cam be passed as an argument to another function

Decorators
----------
A Decorators is a funcation that takes another function as input, adds extra functionality, and returns the 
modified funcation without changing it's original code.
"""

# Calling the funcation without decorator
# def decor(func):
#     def inner(name):
#         if name  == 'sunny':
#             print("Hello sunny bad morning")
#         else:
#             func(name)
#     return inner

# def wish(name):
#     print("Hello", name , "Good Morning")


# decorfun=decor(wish)
# decorfun("sunny")

# Calling the funcation with decorator
def decor(func):
    def inner(name):
        if name  == 'sunny':
            print("Hello sunny bad morning")
        else:
            func(name)

    return inner

@decor
def wish(name):
    print("Hello", name , "Good Morning")


wish("Bhaskar")
wish("sunny")
