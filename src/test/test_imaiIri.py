from unittest import TestCase
import sys
sys.path.append("..")

from main.helper import buildDirectedGraph
from main.gpxParser import parse
from main.imaiIri import removeEdges, getShortestPath
from main.directedGraph import directedGraph, node

class Test(TestCase):

    def test_remove_edges(self):
        points = parse("sample.gpx")
        epsilon = 0.0001
        graph = buildDirectedGraph(points)
        reducedGraph: directedGraph = removeEdges(graph, epsilon)

        if reducedGraph is None:
            self.fail("The returned graph is None ...")

        if len(reducedGraph.getAllNodes()) == 0:
            self.fail("While reducing the graph, no nodes were left ...")

        if len(graph.getAllNodes()[0].getAllSuccessor()) == len(reducedGraph.getAllNodes()[0].getAllSuccessor()):
            self.fail("The reduction of the graph did not work ...")

    def test_get_shortest_path(self):
        points = parse("sample.gpx")
        epsilon = 0.00001
        graph = buildDirectedGraph(points)
        reducedGraph: directedGraph = removeEdges(graph, epsilon)
        shortestPath: list[node] = getShortestPath(reducedGraph)

        if type(shortestPath) != list and not shortestPath is None:
            self.fail("The returned value is not of type list. It is: " + str(type(shortestPath)))

        if len(shortestPath) == 0:
            self.fail("The returned variable does not contain any objects ...")

        print("Test")



if __name__ == "__main__":
    test = Test()
    test.test_get_shortest_path()
    test.test_remove_edges()