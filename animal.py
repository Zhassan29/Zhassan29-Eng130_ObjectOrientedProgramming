# create a class called animal - file name starts with a - class name starts with a
# add the common attributes/var behaviour/functions
# syntax class name: - class animal:

class Animal: # follow the correct naming convention & best practices
    # we need to initialise it with builtin method called __init__(self)
    # self refers current class
    def __int__(self):# any attributes attached to the class should be part of init method
        # self.var = true
        self.alive = True
        self.spine = True
        self.eyes = True

# lets create some methods to add common behaviours
    def breath(self):
        return "keep breathing to stay alive"
    # lets add one more behaviour
    def eat(self):
        return "time to eat"

# create an object of this class
cat = Animal() # this will create object of our Animal class
# print(cat.breath()) # calling a method using object of the Animal class
# print(cat.eat())