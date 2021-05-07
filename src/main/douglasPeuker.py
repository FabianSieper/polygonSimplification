from .helper import computeDistance

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
    realStopIndex = stopIndex if stopIndex > -1 else -1

    listOfPoints = points[realStartIndex : realStopIndex]

    # check if there are still enough points in the list
    if len(listOfPoints) < 3:
        return None

    startPoint = listOfPoints[0]
    endPoint = listOfPoints[-1]

    # if the list is still empty - as least insert the start and the endpoint
    if len(selectedPoints) == 0:
        selectedPoints.append(startPoint)
        selectedPoints.append(endPoint)


    # variables to save the point with the biggest distance
    maxDistance = 0
    mostDistantPoint = -1

    for index, point in enumerate(listOfPoints):
        # compute distance of point
        distance = computeDistance(startPoint, endPoint, point)
        if distance > maxDistance:
            mostDistantPoint = index
            maxDistance = distance

    if maxDistance > epsilon:
        selectedPoints.append(listOfPoints[mostDistantPoint])
        selectedPoints = douglasPecker(points, epsilon, realStartIndex, mostDistantPoint, selectedPoints)

        if not selectedPoints:
            return None

        selectedPoints = douglasPecker(points, epsilon, mostDistantPoint, realStopIndex, selectedPoints)

    return selectedPoints

