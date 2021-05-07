
from helper import buildDirectedGraph
def imaiIri(points, epsilon):
    """
    Performs the imair and Iri algorithm
    :param points: list of lat and long values of points
    :param epsilon: the parameter epsilon of the algorithm from douglas and pecker
    :return: a list of remaining points
            - if a list of points cant be computed under the given preconditions, return None
    """

    # build a directed graph
    # TODO: this function is not fully implemented yet
    directedGraph = buildDirectedGraph(points)

    # each node reaches to all of the next nodes

    # extract each possible path with a maximal hausdorff distance of epsilon
    # finally select the path with the least amount of nodes
