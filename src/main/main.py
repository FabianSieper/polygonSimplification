from douglasPeuker import *
from imaiIri import *
from chanChin import *

import matplotlib.pyplot as plt
import time



def drawPolygon(listOfPoints, label = [], path = None, showImage = True):
    """
    draws a polygon line from the given list of points.
    Stores a image at the given "path" - if no path is given no file will be stored
    :param listOfPoints: a list of points (can be multidimensional)
    :type: last[Point]
    :param label: list of labels according to the list of points
    :type: list(str)
    :param path: path to where the file shall be stored
    :type: str
    :param showImage: shall the drawn image be shown?
    :type: bool
    :return: --
    """

    # if list is only one-dimensional
    if not isinstance(listOfPoints[0], list):
        # transform Point-objects into tuples of floats (with longitude and latitude)
        pointTuples = [(a.getLongitude(), a.getLatitude()) for a in listOfPoints]

        # get separate lists
        longitudes = [point[0] for point in pointTuples]
        latitudes = [point[1] for point in pointTuples]
        plt.plot(longitudes, latitudes)

    else:
        # if list is multidimensional

        for i in range(len(listOfPoints)):

            # transform Point-objects into tuples of floats (with longitude and latitude)
            pointTuples = [(a.getLongitude(), a.getLatitude()) for a in listOfPoints[i]]
            # get separate lists
            longitudes = [point[0] for point in pointTuples]
            latitudes = [point[1] for point in pointTuples]

            plt.plot(longitudes, latitudes)

    plt.axis("off")

    if len(label) > 0:
        plt.legend(label)

    if path:
        plt.savefig(path)

    if showImage:
        plt.show()

def main():
    """
    main function which makes use of all implemented simplification-algorithms
    :return: --
    """
    readPoints = parse("../test/sample.gpx")
    epsilon = 0.0005

    douglas_points = douglasPecker(points=readPoints, epsilon=epsilon)

    imai_points = imaiIri(points=readPoints, epsilon=epsilon)

    chanChin_points = chanChin(points=readPoints, epsilon=epsilon)


    drawPolygon([readPoints, douglas_points], label=["original", "douglas"])

    drawPolygon([readPoints, imai_points], label=["original", "imai"])

    drawPolygon([readPoints, chanChin_points], label=["original", "chanChin"])

    drawPolygon([readPoints, douglas_points, imai_points, chanChin_points], label=["original", "douglas", "imai", "chanChin"])

def measureTime():
    """
    This function uses multiple .gpx files to measure the time required and the amount of nodes chosen for the
    shortcut graphs of each of the algorithms. These measurements then are plotted.
    """

    filePaths = ["gpxFiles/file1.gpx", "gpxFiles/file2.gpx", "gpxFiles/file3.gpx", "gpxFiles/file4.gpx", "gpxFiles/file5.gpx"]

    # read each file and sort them after the size of the file
    sizes = []
    for file in filePaths:
        sizes.append(len(parse(file)))

    # sort the list of files according to the list of sizes
    sizes, filePaths = zip(*sorted(zip(sizes, filePaths)))

    # --------------------------

    # list for the storage of the required times of each of the algorithms
    requiredTimes = []
    # list of the storage of the amount of nodes required for the creation of ech of the shortcut graphs
    amountPoints = []
    epsilon = 0.00005

    # get the execution time of each of the algorithms
    for file in filePaths:

        # read the points from the file
        readPoints = parse(file)

        # measure the time of douglas
        startTime = time.time()
        douglasPoints = douglasPecker(points=readPoints, epsilon=epsilon)
        endTime = time.time()
        durationDouglas = endTime - startTime

        # measure the time of imaiIri
        startTime = time.time()
        imaiIriPoints = imaiIri(points=readPoints, epsilon=epsilon)
        endTime = time.time()
        durationImai = endTime - startTime

        # measure the time of chan & chin
        startTime = time.time()
        chanChinPoints = chanChin(points=readPoints, epsilon=epsilon)
        endTime = time.time()
        durationChanChin = endTime - startTime

        requiredTimes.append({"douglas": durationDouglas, "imai": durationImai, "chanChin": durationChanChin})
        amountPoints.append({"douglas": len(douglasPoints), "imai": len(imaiIriPoints), "chanChin": len(chanChinPoints)})


    # plot the execution times
    # for each of the algorithms
    for alg in requiredTimes[0].keys():

        plt.plot(sizes, [file[alg] for file in requiredTimes])

    plt.title("Processing time")
    plt.ylabel("time in s")
    plt.xlabel("Amount nodes")
    plt.legend(requiredTimes[0].keys())
    plt.show()

    # plot the length of the shortcut graphs
    # for each of the algorithms
    for alg in amountPoints[0].keys():

        plt.plot(sizes, [file[alg] for file in amountPoints])

    plt.title("Amount of nodes in the shortcut graphs")
    plt.ylabel("Amount shortcut nodes")
    plt.xlabel("Amount initial nodes")
    plt.legend(amountPoints[0].keys())
    plt.show()


if __name__ == "__main__":
    main()
    measureTime()