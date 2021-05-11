from unittest import TestCase

import sys
sys.path.append("../main")
from gpxParser import parse

class Test(TestCase):
    def test_parse(self):

        solution = parse("sample.gpx")
        if type(solution) != list:
            self.fail("The given solution is not of type list!")

        print(solution)

if __name__ == "__main__":
    test = Test()
    test.test_parse()