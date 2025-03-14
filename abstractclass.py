# import necessary packages
from abc import ABC,abstractmethod
# create a base class
class Animal (ABC):
        #abstract method
        # should be implemented by all sub-class 
        def move(self):
                pass
class Human (Animal):
        def move(self):
            print("I can walk and run")
class Snake (Animal):
        def move(self):
            print("I can crawl")
class Dog (Animal):
        def move(self):
            print("I can bark")
class Lion (Animal):
       def move(self):
              print("I Can ROAR")

#Drivers Code
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()