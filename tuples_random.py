from collections import namedtuple
from random import randint, random

color=namedtuple("color","red, green, blue, alpha")
def random_color():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    alpha = round(random(),2)
    return color(red, green, blue, alpha)

if __name__ == "__main__":
    color=random_color()
    print(color)