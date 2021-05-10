import sys
sys.path.append("../main")

from helper import buildDirectedGraph, computeDistance
from directedGraph import directedGraph, node
from tqdm import tqdm
import copy

def imaiIri(points, epsilon):
    """
    Performs the imair and Iri algorithm
    :param points: list of lat and long values of points
    :param epsilon: the parameter epsilon of the algorithm from douglas and pecker
    :return: a list of remaining points
            - if a list of points cant be computed under the given preconditions, return None
    """

    # build a directed graph
    directedGraph = buildDirectedGraph(points)

    # extract each possible path with a maximal hausdorff distance of epsilon
    reducedGraph = removeEdges(directedGraph, epsilon)

    # finally select the path with the least amount of nodes
    return getShortestPath(reducedGraph)


def getShortestPath(graph: directedGraph):
    """
    Selects the shortest path between the head and the tail of the graph
    :param graph: the first element of a directedGraph
    :type: directedGraph
    :return: list of points, which in summary are the shortest connection between the head and the last leaf of the graph
    """

    # easy solution
    shortestPath: list[node] = [graph.getHead()]

    while True:
        if len(shortestPath[-1].getAllSuccessor()) == 0:
            break
        else:
            shortestPath.append(shortestPath[-1].getAllSuccessor()[-1])


    return shortestPath


def removeEdges(directedGraph, epsilon):
    """
    Checks for each shortcut-edge in the graph, if the error of the shortcut is at max "epsilon".
    Removes all edges with error > "epsilon"
    :param directedGraph: a directed graph instance
    :type: directedGraph
    :param epsilon: the maximal allowed error
    :type: float
    :return: a directed graph
    """

    copiedDirectedGraph = copy.deepcopy(directedGraph)

    for index_node, node in enumerate(tqdm(copiedDirectedGraph.getAllNodes()[0:-1])):

        successors = node.getAllSuccessor()

        # check if shortcut from node to successor creates a smaller mistake than "epsilon"
        startPoint = node.getValue()

        listOfIndexes = []
        for index_succ, succ in enumerate(successors):

            # if a successor was already removed - continue
            # (this is just for safety)
            if succ is None:
                continue

            # compute the error made
            for distantPoint in successors[0: index_succ]:
                error = computeDistance(startPoint, succ.getValue(), distantPoint.getValue())

                # if the error is too big
                if error > epsilon:
                    # save index at which the successor shall be removed so those nodes can be removed later on
                    listOfIndexes.append(index_succ)
                    # break out of the loop of between-points, as only one distance has to be > epsilon ...
                    # and that case was already found
                    break

        copiedDirectedGraph.getAllNodes()[index_node].removeMultipleSuccessors(listOfIndexes)

    return copiedDirectedGraph