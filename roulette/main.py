import random


def roulette(*choices):
    choice_list = [i for i in choices]
    x = choice_list[random.randrange(len(choice_list))]
    return x
