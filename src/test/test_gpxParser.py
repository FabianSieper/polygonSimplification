from unittest import TestCase
from project.src.main.gpxParser import parse

class Test(TestCase):
    def test_parse(self):

        solution = parse("sample.gpx")
        if type(solution) != list:
            self.fail("The given solution is not of type list!")

        print(solution)

