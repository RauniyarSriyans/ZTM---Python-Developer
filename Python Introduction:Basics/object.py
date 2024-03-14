class User(object):
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('logged in')

class PlayerCharacter(User):
    # class object attribute, not dynamic, can't be modified 
    membership = True 

    def __init__(self, name, age, email):
        # super allows to initialize the parent class and access parents' class methods too 
        super().__init__(email)
        self.name = name # attribute
        # private variable when underscore is used
        self._age = age
    
    def run(self):
        print('run')
    
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def sum(*args):
        return sum(args)

player1 = PlayerCharacter("shree", 22, 'my@gmail.com')
player1.run()

# checks if player1 is an instance of the class PlayerCharacter
print(isinstance(player1, PlayerCharacter))

# prints out all methods of player1 class
# introspection
print(dir(player1))