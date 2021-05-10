from directedGraph import *
from douglasPeuker import *
from gpxParser import *
from helper import *
from imaiIri import *

import argparse
import matplotlib.pyplot as plt

def getFilePath():
    """
    Reads command line arguments
    :return: file, from which the data shall be read, or None if no arg was found
    """

    parser = argparse.ArgumentParser(description="Simplification of polygons")
    parser.add_argument('-o', "--file", help = "Path to an .gpx file")

    args = parser.parse_args()

    if args.file:
        return args.file

    print("INFO - No file was given by the command line - using default file for further processing ...")
    return "../test/sample.gpx"


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
    filePath = getFilePath()
    readPoints = parse(filePath)

    epsilon_douglas = 0.001
    douglas_points = douglasPecker(points=readPoints, epsilon=epsilon_douglas)

    epsilon_imai = 0.0001
    imai_nodes = imaiIri(points=readPoints, epsilon=epsilon_imai)
    imai_points = [imai.getValue() for imai in imai_nodes]


    drawPolygon([readPoints, douglas_points, imai_points], label=["original", "douglas", "imai"])


if __name__ == "__main__":
    main()