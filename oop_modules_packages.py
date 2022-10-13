# lucky draw
# import - imports from external libraries folder on the left
import random      # allows us to generate something random
#print(random.random()) # prints a random number each time - calls the random folder

from random import *       # from this flder import this
#print(random())


import math
number = 23.9
#round numbers .5 and above up
#numbers.49 and below round down
#print(math.ceil(number))        # ceil rounds everything up
#print(math.floor(number))       # floor rounds everything down


import datetime, sys
import os
#print(os.cpu_count()) # this will result in number cpu based on your os
#print(datetime.date.today()) # this will result todays date based on your os
#print(sys.path)


# dont repeat yourself (dry)
# reusable - saves time - saves money
# lets build some functions
# syntax def name(): - def name(): - def name:
#def greeting():
    # greet the user
    #print("hello dear")

    #pass

# unless the function is called it does nothing
#greeting()

# greet the user with their name

#def greet_user(name): # create a function that takes an arg - the name
    #print("hello dear " + name) # adding 2 string with user input()
    #pass
#greet_user("zak")


# lets create a function that take int as an args
def add(value1, value2): # take user input as int then  add them together display the outcome
    print("this function is to provide addition functionality")
# return statement
    return value1 + value2
# if you are using a return statement and calling the function - it needs to be in a print statement.
print(add(2, 2))














