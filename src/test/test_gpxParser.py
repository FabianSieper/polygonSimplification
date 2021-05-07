from unittest import TestCase
from ..main.gpxParser import parse
from .. main.gpxParser import Point
class Test(TestCase):
    def test_parse(self):

        solution = parse("src/test/sample.gpx")
        if type(solution) != list:
            self.fail("The given solution is not of type list!")

        print(solution)

