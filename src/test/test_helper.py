from unittest import TestCase
import sys
sys.path.append("../main")

from gpxParser import Point
from helper import computeDistance, buildDirectedGraph
from gpxParser import parse

import random


class Test(TestCase):
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
        try:

            for i in range(100):
                startPoint = Point(random.random(), random.random())
                endPoint = Point(random.random(), random.random())
                distantPoint = Point(random.random(), random.random())

                _ = computeDistance(startPoint, endPoint, distantPoint)

        except Exception as e:
            self.fail("An exception occured while trying to compute distances for random points:")
            print(e)

    def test_build_directed_graph(self):

        listOfPoints = parse("sample.gpx")

        graph = buildDirectedGraph(listOfPoints)

        if len(graph.getAllNodes()) == 0:
            self.fail("No nodes were added to the list of all nodes while creating a directed graph ...")


if __name__ == "__main__":
    test = Test()
    test.test_compute_distance()
    test.test_build_directed_graph()