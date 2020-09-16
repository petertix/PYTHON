#!/usr/bin/python
""" Calculate circle stuff """


import math
import sys


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    while True:
        try:
            r = input("\nEnter a Radius for a circle: ")
            # r = int(r)
        except (ValueError, SyntaxError, NameError, TypeError):
            print("You need to type in a valid number!\n")
            sys.exit()

        # Instantiate a Circle Object
        a = Circle(r)

        print("Radius: {0}  Area: {1}  Circumference: {2}".format(r, a.area(),
              a.circumference()))
