from unittest import TestCase

from project.src.main.helper import buildDirectedGraph
from project.src.main.gpxParser import parse
from project.src.main.imaiIri import removeEdges

class Test(TestCase):
    # TODO
    def test_imai_iri(self):
        pass

    def test_remove_edges(self):
        points = parse("sample.gpx")
        epsilon = 0.0001
        graph = buildDirectedGraph(points)
        reducedGraph = removeEdges(graph, epsilon)

        if reducedGraph is None:
            self.fail("The returned graph is None ...")

        if len(reducedGraph.getAllNodes()) == 0:
            self.fail("While reducing the graph, no nodes were left ...")

        print(len(graph.getAllNodes()[0].getAllSuccessor()))
        print(len(reducedGraph.getAllNodes()[0].getAllSuccessor()))
        if len(graph.getAllNodes()[0].getAllSuccessor()) == len(reducedGraph.getAllNodes()[0].getAllSuccessor()):
            self.fail("The reduction of the graph did not work ...")