

def imaiIri(points, epsilon, startIndex = -1, stopIndex = -1, selectedPoints = []):
    """
    Performs the imair and Iri algorithm
    :param points: list of lat and long values of points
    :param epsilon: the parameter epsilon of the algorithm from douglas and pecker
    :param startIndex: Index at which the algorithm shall start
                        - if set to -1 the algorithm will start at the beginning of the list
    :param stopIndex: Index at which the algorithm will stop
                        - if set to -1 the algorithm will stop at the end of the list
    :param selectedPoints: A list of points, which were already selected by the algorithm
                        - this list will be returned at the end
    :return: a list of remaining points
            - if a list of points cant be computed under the given preconditions, return None
    """

    # build a directed graph
    # each node reaches to all of the next nodes

    # extract each possible path with a maximal hausdorff distance of epsilon
    # finally select the path with the least amount of nodes
