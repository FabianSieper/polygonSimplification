
import sys
sys.path.append("../main")

from helper import computeDistance

def douglasPecker(points, epsilon, startIndex = -1, stopIndex = -1, selectedPoints = []):
    """
    Performs the douglas and pecker algorithm
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

    # get which start and endpoint shall be used
    realStartIndex = startIndex if startIndex > -1 else 0
    realStopIndex = stopIndex if stopIndex > -1 else len(points)


    listOfPoints = points[realStartIndex:realStopIndex]


    # check if there are still enough points in the list to optimize a path
    if len(listOfPoints) < 3:
        selectedPoints.extend(listOfPoints)
        return selectedPoints

    startPoint = listOfPoints[0]
    endPoint = listOfPoints[-1]

    # if the list is still empty - as least insert the start and the endpoint
    if len(selectedPoints) == 0:
        selectedPoints.append(startPoint)
        selectedPoints.append(endPoint)


    # variables to save the point with the biggest distance
    maxDistance = 0
    mostDistantPoint = -1

    for i in range(realStartIndex, realStopIndex, 1):
        point = points[i]
        # compute distance of point
        distance = computeDistance(startPoint, endPoint, point)
        if distance > maxDistance:
            mostDistantPoint = i
            maxDistance = distance

    if maxDistance > epsilon:
        # append the point with the furthest distance to the solution trajectory
        if not points[mostDistantPoint] in selectedPoints:
            selectedPoints.append(points[mostDistantPoint])

        # get the best simplification for a part of the trajectory

        selectedPoints = douglasPecker(points, epsilon, realStartIndex, mostDistantPoint, selectedPoints)

        # get the best simplification for the second part of the trajectory
        selectedPoints = douglasPecker(points, epsilon, mostDistantPoint, realStopIndex, selectedPoints)

    # sort list after the index of each of the points (the new path has to be in the same order as the old one)
    selectedPoints = sorted(selectedPoints, key=lambda pt: pt.getIndex())
    return selectedPoints

