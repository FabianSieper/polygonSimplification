from unittest import TestCase
from ..main.douglasPeuker import *
from ..main.gpxParser import *
from ..main.helper import *
import random

class Test(TestCase):
    def test_douglas_pecker(self):

        points = parse("src/test/sample.gpx")
        epsilon = 0.119
        solution = douglasPecker(points, epsilon)

        if type(solution) != list and solution != None:
            self.fail("The returned value is not of type list. Is: " + str(type(solution)))

        print(len(points))
        print(len(solution) if solution != None else None)

