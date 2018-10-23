#################################################################################
# Name: Dostonbek Toirov
# Username: toirovd
#
# Purpose: Creating interactive virtual pets
#################################################################################
# Acknowledgements:
#
#
#################################################################################

from owner import *
from pygame import mixer
import time


def main():
    '''
    main game loop occurs here
    :return:
    '''
    mixer.init()        # initializing mixer to play sounds

    name = input("What is your name, Pet Lover? : ")
    owner = Owner(name)
    owner.greet(name)
    owner.buy()
    owner.name_it()
    owner.color_it()
    owner.give_age()

    # game loop
    while True:
        # checking hunger level
        owner.pet[0].hunger = True
        owner.pet[0].hunger_level()
        # feeding the pet
        food = owner.feed()
        print("Your " + owner.pet[0].name + " likes " + food)
        print("Your pet is full now!!!")
        time.sleep(3)
        print()
        # taking the pet to the bathroom
        owner.pet[0].bathroom()
        print()
        time.sleep(10)
        # taking the pet to bed
        owner.pet[0].sleep()
        time.sleep(10)
        print()
        print()
        # pet wakes up, and the loop starts over
        print("Oh, no!!! Your pet woke up!!!")
        time.sleep(2)


if __name__ == '__main__':
    main()
