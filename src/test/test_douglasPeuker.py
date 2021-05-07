from unittest import TestCase
from ..main.douglasPeuker import *
from ..main.gpxParser import *

import random
import traceback

class Test(TestCase):
    def test_douglas_pecker(self):

        points = parse("src/test/sample.gpx")
        epsilon = 0.119
        solution = douglasPecker(points, epsilon)

        if type(solution) != list and solution != None:
            self.fail("The returned value is not of type list. Is: " + str(type(solution)))

        print(len(points))
        print(len(solution) if solution != None else None)

    def test_compute_distance(self):

        startPoint = Point(0, 1)
        endPoint = Point(2, 1)
        distantPoint = Point(1, 2)

        expectedSolution = 1.
        computedSolution = computeDistance(startPoint, endPoint, distantPoint)

        if expectedSolution != computedSolution:
            self.fail("The computed distance does not match the expected distance!")

        # -

        startPoint = Point(0, 1)
        endPoint = Point(2, 1)
        distantPoint = Point(3, 1)

        expectedSolution = 1.
        computedSolution = computeDistance(startPoint, endPoint, distantPoint)

        if expectedSolution != computedSolution:
            self.fail("The computed distance does not match the expected distance!")

        # -

        startPoint = Point(0, 1)
        endPoint = Point(2, 1)
        distantPoint = Point(1, -1)

        expectedSolution = 2.
        computedSolution = computeDistance(startPoint, endPoint, distantPoint)

        if expectedSolution != computedSolution:
            self.fail("The computed distance does not match the expected distance!")

        # -

        # test for random inputs: no exception should be thrown
        for i in range(100):
            try:
                startPoint = Point(random.random(), random.random())
                endPoint = Point(random.random(), random.random())
                distantPoint = Point(random.random(), random.random())

                _ = computeDistance(startPoint, endPoint, distantPoint)

            except Exception as e:
                self.fail("An exception occured while trying to compute distances for random points:")
                print(e)