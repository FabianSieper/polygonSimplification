from unittest import TestCase
import sys
sys.path.append("..")

from main.douglasPeuker import *
from main.gpxParser import *


class Test(TestCase):
    def test_douglas_pecker(self):

        points = parse("sample.gpx")
        epsilon = 0.119
        solution = douglasPecker(points, epsilon)

        if type(solution) != list and solution != None:
            self.fail("The returned value is not of type list. Is: " + str(type(solution)))

        print(len(points))
        print(len(solution) if solution != None else None)

if __name__ == "__main__":
    test = Test()
    test.test_douglas_pecker()