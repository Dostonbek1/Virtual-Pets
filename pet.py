import time
from pygame import mixer

class Pet:

    def __init__(self, type):
        '''
        Initializing the attributes of class Pet
        :param type:
        '''
        self.type = type
        self.name = None
        self.color = None
        self.hunger = False
        self.food = None
        self.age = 0

    def sleep(self):
        '''
        Used to make the pet go to bed
        :return:
        '''
        print("Now your " + self.name + " wants to sleep")
        sleep = input("Write 'sleep' to take your pet to bed: ")
        time.sleep(2)
        print("Now your " + self.name + " is sleeping...")
        # play snoring sound
        mixer.music.load('snore.mp3')
        mixer.music.play()

    def hunger_level(self):
        '''
        Checks the hunger level of the pet, and if hungry, tells it to the owner.
        :return:
        '''
        if self.hunger == True:
            print()
            print("Your pet is hungry!!!")
            print("S/He needs to eat!!!")

    def eat(self, food):
        '''
        Turns the hunger attribute to False.
        :param food:
        :return:
        '''
        self.hunger = False

    def bathroom(self):
        '''
        Used to take the pet to the bathroom.
        :return:
        '''
        print("Your pet " + self.name + " wants to go to bathroom!!!")
        # play growling sound
        mixer.music.load('growling.mp3')
        mixer.music.play()
        go = input("Write 'go' to take him to the bathroom: ")
        time.sleep(2)
        if go == "go":
            # play bathroom sound
            mixer.music.load('flush.mp3')
            mixer.music.play()
            print("You have saved your pet!!! S/He is happy with you now!!!")
        else:
            self.bathroom()
