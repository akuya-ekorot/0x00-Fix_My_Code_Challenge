#!/usr/bin/python3
""" This module defines a class Square """


class Square:
    """ A class to represent a square """

    size = 0

    def __init__(self, size=0):
        """ Constructor method """
        self.size = size

    def area_of_my_square(self):
        """ Area of the square """
        return self.size * self.size

    def permiter_of_my_square(self):
        return (self.size * 4)

    def __str__(self):
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":

    s = Square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
