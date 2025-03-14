# import necessary packages
from abc import ABC,abstractmethod

#Create Base class
class Absclass(ABC):


    def print(self, x):
        print("Passed Value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside of Absclass task")


class test_class(Absclass):
        def task(self):
            print("We are inside test_class task")


test_obj = test_class()
test_obj.task()
test_obj.print(100)