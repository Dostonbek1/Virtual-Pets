from pet import *

class Owner:
    '''
    Owner class. Used to create instances of an owner
    '''
    def __init__(self, name):
        '''
        Initializing the owner attributes
        :param name:
        '''
        self.name = name
        self.pet = []

    def greet(self, name):
        '''
        Greetings with the owner
        :param name:
        :return:
        '''
        print("Hello, " + name + "!")
        print("Now you are going to be a pet owner.")
        print("And you will need to take of your pet!")
        print("Be responsible!")
        print()

    def buy(self):
        '''
        Adds a new instance of a pet class
        :return:
        '''
        type = input("What pet would you like to buy? : ")
        self.pet.append(Pet(type))
        print("You have bought a " + type)

    def name_it(self):
        '''
        Names the pet
        :return:
        '''
        name = input("Please, give a name to it: ")
        self.pet[0].name = name
        print("You have named it " + name + ". Congrats!")
        print()

    def color_it(self, ):
        '''
        Gives a color to the pet
        :return:
        '''
        color = input("What color do you want your " + self.pet[0].name + " to be? : ")
        self.pet[0].color = color
        print("Now your " + self.pet[0].name + " is " + color + " in color.")
        print()

    def give_age(self):
        '''
        Defines the age of the pet
        :return:
        '''
        age = input("What age do you want it to be? : ")
        self.pet[0].age = age
        print("Your " + self.pet[0].name + " is now " + age + " years old.")
        print()
        time.sleep(2)

    def feed(self):
        '''
        Feeds the pet. Uses the eat method of the pet
        :return:
        '''
        food = input("What do you want to feed your pet with? : ")
        self.pet[0].eat(food)
        return food
