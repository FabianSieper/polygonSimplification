import sys
sys.path.append("../main")

from gpxParser import *
from directedGraph import directedGraph, node

from copy import deepcopy
import numpy as np

def getWedge(point1, point2, epsilon):
    """
    Takes two points, and computes the wedge from point1 to point2 such that
    a circle with radius epsilon around point2 fits in that wedge
    :param point1: start point
    :type: Point
    :param point2: end point
    :type: Point
    :param epsilon: radius
    :return: tuple of float (degrees) in between which the wedge is (the first parameter is always bigger than the second one)
    """

    numpPoint2 = np.array([point2.x(), point2.y()])
    numpPoint1 = np.array([point1.x(), point1.y()])

    # compute vector from point 1 to point 2
    vec1To2 = np.array([point2.x() - point1.x(), point2.y() - point1.y()])

    # compute the orthogonal vector of the vector between the two points
    orthVec = np.array([vec1To2[1], vec1To2[0] * -1])

    # compute the normalized vector of the orthogonal vector
    normOrthVec = orthVec / np.sqrt(np.sum(np.power(orthVec, 2)))

    # check if normalization of vector is working correctly

    assert len(normOrthVec) == 2 and np.round(np.sqrt(np.power(normOrthVec[0], 2) + np.power(normOrthVec[1], 2)), 5) == 1.
    # check if both vectors are still orthogonal to each other
    assert np.round(normOrthVec[0] * vec1To2[0] + normOrthVec[1] * vec1To2[1], 5) == 0

    # as the radius around point 2 is "epsilon", so shall the length of the normalized vector be
    epsiVec = normOrthVec * epsilon
    assert np.round(np.sqrt(np.power(epsiVec[0], 2) + np.power(epsiVec[1], 2)), 5) == np.round(epsilon, 5)

    # add and subtract vector from point 2 to get two points which describe the outer bounds of the wedge
    outerPoint1 = numpPoint2 + epsiVec
    outerPoint2 = numpPoint2 - epsiVec


    # compute vectors to outer points
    outVec1 = outerPoint1 - numpPoint1
    outVec2 = outerPoint2 - numpPoint1

    # compute degrees in the unit circle from these two vectors
    deg1 = np.arctan2(outVec1[1], outVec1[0]) * 180 / np.pi
    deg2 = np.arctan2(outVec2[1], outVec2[0]) * 180 / np.pi

    return (deg1, deg2) if deg1 > deg2 else (deg2, deg1)


def makeWedgeCut(wedge1, wedge2):
    """
    Takes two wedges (two tuples of angles) and computes a new wedge, which is the intersection of both cuts
    :param wedge1: range of angles (first angle has to be larger than the second one)
    :type: (float, float)
    :param wedge2: range of angles (first angle has to be larger than the second one)
    :type: (float, float)
    :return: a wedge
    :type: (float, float)
    """

    assert wedge1[0] > wedge1[1] and wedge2[0] > wedge2[1], "The first angle in tuple has to be bigger than second one"

    # check if they even intersect
    if not (wedge1[0] > wedge2[0] and wedge2[0] > wedge1[1]) and not (wedge2[0] > wedge1[0] and wedge1[0] > wedge2[1]):
        return (0, 0)

    # take the smaller value of the big values (index 0) and the bigger value of the small values (index 1)
    return (wedge1[0] if wedge1[0] < wedge2[0] else wedge2[0], wedge1[1] if wedge1[1] > wedge2[1] else wedge2[1])


# TODO: this function is not ready yet
def buildGraph(points, epsilon):
    """
    Builds directed graph G from the list of points
    :param points: list of lat and long values of points
    :param epsilon: the parameter epsilon of the algorithm from douglas and pecker
    :return: a directed shortcut graph
    :type: directedGraph
    """

    # this list will be extended iteratively
    shortcutGraph = directedGraph()

    # compute intersection in which the next points lays
    # for each of the nodes between the start and the end node
    for i in range(1, len(points) - 1, 1):

        startPoint = points[i]
        startNode = node(startPoint)

        # initial wedge
        wedge = [360, 0]

        # for each point from 'startPoint' till end
        for j in range(i + 1, len(points), 1):

            # compute wedge
            newWedge = getWedge(startPoint, points[j], epsilon)
            # cut wedge with existing wedge
            wedge = makeWedgeCut(wedge, newWedge)

            # if cut is empty -> break
            if wedge[0] == 0. and wedge[1] == 0.:
                break

            else:
                # if cut is not empty and still not the last point -> continue
                startNode.addSuccessor(node(points[j]))


        # append the new node to the shortcut graph
        shortcutGraph.addNode(startNode)

        # if cut is not empty and last point -> add last point to shortcut graph

    # add last point to shortcut graph
    shortcutGraph.addNode(node(points[-1]))

    return shortcutGraph

def createCutBetweenDirGraphs(graph1, graph2):
    """
    Takes two directed graphs, cuts them and returns a directed graph which only contains those edges
    which are contained in both graphs (independent of the direction)
    :param graph1: directed graph 1
    :type: directedGraph
    :param graph2: directed graph 2
    :type: directedGraph
    :return: a directed graph
    :type: directedGraph
    """

    # make sure to not change values outside of the function (pure function)
    graph1 = deepcopy(graph1)
    graph2 = deepcopy(graph2)

    # will be modified and returned later on
    outputGraph = directedGraph()

    # sort the nodes in the graphs
    graph1.sortNodes(lambda a: a.getValue().getIndex())
    graph2.sortNodes(lambda a: a.getValue().getIndex())

    for i in range(len(graph1.getAllNodes())):

        # for each node of graph 1
        startNode: node = graph1.getAllNodes()[i]
        correctedNode: node = deepcopy(startNode)

        for j in range(len(startNode.getAllSuccessor())):

            # and for each of the connections of the startNode
            endNode: node = startNode.getAllSuccessor()[j]

            # get endNode in graph2
            startNodeGraph2: node = graph2.getAllNodes()[graph2.getAllNodes().index(endNode)]

            # if same connection (but reversed) does not exists in graph2,
            if not (startNode in startNodeGraph2.getAllSuccessor()):
                # then remove that connection in graph1
                correctedNode.removeSuccessor(endNode)

        # add node which only contains the right connections to the output graph
        outputGraph.addNode(correctedNode)

    return outputGraph



def chanChin(points: [Point], epsilon: float):
    """
    Performs the chan and chin algorithm on a polygon
    :param points: list of lat and long values of points
    :param epsilon: the parameter epsilon of the algorithm from douglas and pecker
    :return: a list of remaining points
    """

    points = deepcopy(points)

    # compute Graph G_prime and G_prime_prime (backwards):
    gPrime = buildGraph(points, epsilon)

    # reverse the list of points in order to reverse the build directed graph
    points.reverse()
    gPrimeInverse = buildGraph(points, epsilon)

    # get cut between graphs G_prime and G_prime_prime
    # TODO: the first node of the graph has no connection to the next node
    cutGraph = createCutBetweenDirGraphs(gPrime, gPrimeInverse)

    # TODO: remove these lines:
    if len(cutGraph.getAllNodes()[0].getAllSuccessor()) == 0:
        print("ERROR - The first node does not has a single connection")
        exit()

    # find shortest path in linear time
    shortestPathNodes = cutGraph.findShortestPath()

    # transform list of nodes into list of points
    shortesPathPoints = [nodeInst.getValue() for nodeInst in shortestPathNodes]

    # return list of points
    return shortesPathPoints