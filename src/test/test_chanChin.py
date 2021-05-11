from unittest import TestCase
import sys

sys.path.append("../main")

from chanChin import buildGraph, getWedge, makeWedgeCut, createCutBetweenDirGraphs
from gpxParser import parse, Point
from directedGraph import directedGraph
from main import drawPolygon

import numpy as np
import random


class Test(TestCase):
    def test_build_graph(self):
        points = parse("sample.gpx")
        epsilon = 0.119
        graph: directedGraph = buildGraph(points, epsilon)

        if graph is None:
            self.fail("None was returned!")

        if len(graph.getAllNodes()) == 0:
            self.fail("The graph is empty and does not contain any nodes.")

    def test_get_wedge(self):
        point1 = Point(1, 2)
        point2 = Point(3, 5)
        epsilon = 0.3

        wedge = getWedge(point1, point2, epsilon)

        if type(wedge) != tuple:
            self.fail("The returned value is not of type tuple! Is of type: " + str(type(wedge)))

        if type(wedge[0]) != float and type(wedge[0]) != np.float64:
            self.fail("The returned value inside of the tuple is not of type float! Is of type: " + str(type(wedge[0])))

        if len(wedge) != 2:
            self.fail("The returned tuple does not has a size of 2! Size is: " + str(len(wedge)))

        if wedge[0] < wedge[1]:
            self.fail("The first element of the returned tuple always has to be bigger or equal to the second value. "
                      "Values are: " + str(wedge))

    def test_make_wedge_cut(self):
        point1 = Point(1, 2)
        point2 = Point(3, 5)
        point3 = Point(-1, -2)
        point4 = Point(3.24961509, 4.83358994)
        epsilon = 0.3

        wedge1 = getWedge(point1, point2, epsilon)
        wedge2 = getWedge(point1, point3, epsilon)

        cut1 = makeWedgeCut(wedge1, wedge2)

        if cut1[0] != cut1[1]:
            self.fail("The cut should be empty, but is not. Cut is: " + str(cut1))

        wedge3 = getWedge(point1, point4, epsilon)
        cut2 = makeWedgeCut(wedge1, wedge3)

        if len(cut2) != 2:
            self.fail("The length of the tuple is not 2. Length is: " + str(len(cut2)))

        if cut2[0] == cut2[1]:
            self.fail("The wedge should not have a range of zero! Cut is: " + str(cut2))

        # make 100 random wedges
        for i in range(100):
            point1 = Point(random.random(), random.random())
            point2 = Point(random.random(), random.random())
            epsilon = random.random() + 0.01

            wedge1 = getWedge(point1, point2, epsilon)

            if wedge1 is None:
                self.fail("The wedge should not be None!")


    def test_create_cut_between_dir_graphs(self):


        point1 = Point(1, 2)
        point2 = Point(1, 3)
        point3 = Point(1, 4)
        point4 = Point(4, 4)
        epsilon = 0.5


        graph1: directedGraph = buildGraph([point1, point2, point3, point4], epsilon)

        graph2: directedGraph = buildGraph([point4, point3, point2, point1], epsilon)


        cutGraph = createCutBetweenDirGraphs(graph1, graph2)

        if len(cutGraph.getAllNodes()) != 4:
            self.fail("The cut graph should have exactly four nodes!")


        # --
        points: [Point] = parse("sample.gpx")
        epsilon = 0.0005

        graph1: directedGraph = buildGraph(points, epsilon)

        # reverse the order of the points to build an inverse graph
        points.reverse()
        graph2: directedGraph = buildGraph(points, epsilon)

        cutGraph = createCutBetweenDirGraphs(graph1, graph2)

        shortestPath = cutGraph.findShortestPath()

        print(len(cutGraph.getAllNodes()))
