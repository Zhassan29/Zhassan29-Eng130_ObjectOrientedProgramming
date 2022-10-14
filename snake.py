from reptile import Reptile

class snake(Reptile):
    def __int__(self):
        super().__int__()
        self.forked_tongue = True

    def use_tongue_to_smaell(self):
        return "if i can touch it i can smell it as well"

smart_snake = snake()
print(f"this function is called from parent {smart_snake.hunt()}")
print(f"this function is called from the current class {smart_snake.use_tongue_to_smaell()}")
print(f"this function is called from grand parent class {smart_snake.eat()}")