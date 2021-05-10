
import gpxpy
import gpxpy.gpx


class Point:

    def __init__(self, longitude, latitude, index = -1):
        """
        Initialization of points
        :param longitude: the value of the longitude of a point
        :param latitude: the value of the latitude of a point
        :param index: an index which describes at which time the point was created
                        - this allows to sort a potential list when removing and adding points to it
        """
        self.longitude = longitude
        self.latitude = latitude
        self.index = index

    def getLongitude(self):
        return self.longitude

    def getLatitude(self):
        return self.latitude

    def x(self):
        return self.latitude

    def y(self):
        return self.longitude

    def getIndex(self):
        return self.index

    def __eq__(self, other):

        if self.latitude == other.getLatitude() and self.longitude == other.getLongitude() and self.index == other.getIndex():
            return True

        return False

def parse(filepath):
    """
    :param filepath: path to a .gpx file
    :return: a list of points, containing latitude, longitude
    """
    readPoints = []
    with open(filepath, "r") as gpx_file:
        gpx = gpxpy.parse(gpx_file)

        index = 0
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    readPoints.append(Point(point.longitude, point.latitude, index))
                    index += 1

        # if there were no points in a track or if there was no defined track
        # instead read waypoints
        if len(readPoints) == 0:
            print("INFO - No track found - reading waypoints instead ...")
            for waypoint in gpx.waypoints:
                readPoints.append(Point(waypoint.longitude, waypoint.latitude, index))
                index += 1

    return readPoints