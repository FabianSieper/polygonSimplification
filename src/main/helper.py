from .gpxParser import Point
from .directedGraph import *

import math
def computeDistance(startPoint: Point, endPoint: Point, distantPoint: Point):
    """
    Computes the distance between a line (start and endpoint) and a point (distantPoint)
    :param startPoint: point at which the line starts
    :param endPoint: point at which the line ends
    :param distantPoint: point whos distance shall be computed
    :return: distance from the point to the line between start- and endpoint
    """

    # check if the points all have the same longitude or latitude
    if startPoint.x() == endPoint.x() and endPoint.x() == distantPoint.x():

        dist1 = abs(startPoint.y() - distantPoint.y())
        dist2 = abs(endPoint.y() - distantPoint.y())
        return dist1 if dist1 < dist2 else dist2

    elif startPoint.y() == endPoint.y() and endPoint.y() == distantPoint.y():

        dist1 = abs(startPoint.x() - distantPoint.x())
        dist2 = abs(endPoint.x() - distantPoint.x())
        return dist1 if dist1 < dist2 else dist2


    return abs((abs((endPoint.x() - startPoint.x()) * (startPoint.y() - distantPoint.y()) -
                    (startPoint.x() - distantPoint.x()) * (endPoint.y() - startPoint.y())) /
                    math.sqrt(math.pow(endPoint.x() - startPoint.x(), 2) + math.pow(endPoint.y() - startPoint.y(), 2))))



def buildDirectedGraph(listOfPoints):
    """
    Computes a directed graph from the given list. Each Point points to all of if successors
    :param listOfPoints: a list of Points
    :return: a directed graph
    """
    pass