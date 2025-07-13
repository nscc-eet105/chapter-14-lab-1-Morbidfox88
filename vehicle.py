#Chad Collard
#Chapter 14 Lab 1
#Vehicle class
#7/12/2025

class Vehicle:

    def __init__(self, name, year, model):
        self.__name = name
        self.__year = year
        self.__model = model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 1
        print(f'The {self.__name} {self.__model} is Accelerating...')
        return f'The {self.__name} {self.__model} is accelerating to {self.__speed} mph'

    def decelerate(self):
        self.__speed -= 1
        if  self.__speed < 0:
            self.__speed = 0  
        print(f'The {self.__name} {self.__model} is Decelerating...')
        return f'The {self.__name} {self.__model} is decelerating to {self.__speed} mph'

    def get_speed(self):
        return self.__speed

    def __str__(self):
        return f'This is a {self.__year} Black {self.__name} {self.__model} with a current speed of {self.__speed} mph'
