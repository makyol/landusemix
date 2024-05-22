import unittest
from landusemix import LandUseMixIndices
import math


class TestLandUseMixIndices(unittest.TestCase):

    def setUp(self):
        self.land_use_areas = {
            "residential": 500,
            "commercial": 300,
            "industrial": 200
        }
        self.indices = LandUseMixIndices(self.land_use_areas)

    def test_entropy_index(self):
        expected = -sum((area / 1000) * math.log(area / 1000)
                        for area in [500, 300, 200]) / math.log(3)
        print("Expected entropy index:", expected)
        self.assertAlmostEqual(self.indices.entropy_index(), expected)

    def test_herfindahl_hirschman_index(self):
        expected = sum((100 * (area / 1000)) ** 2 for area in [500, 300, 200])
        print("Expected Herfindahl-Hirschman index:", expected)
        self.assertAlmostEqual(
            self.indices.herfindahl_hirschman_index(), expected)

    def test_entropy_index_single_land_use(self):
        land_use_areas = {
            "residential": 1000
        }
        indices = LandUseMixIndices(land_use_areas)
        expected = 0.0
        print("Expected entropy index for single land use:", expected)
        self.assertAlmostEqual(indices.entropy_index(), expected)

    def test_entropy_index_equal_area(self):
        land_use_areas = {
            "residential": 500,
            "commercial": 500,
            "industrial": 500
        }
        indices = LandUseMixIndices(land_use_areas)
        expected = -sum((area / 1500) * math.log(area / 1500)
                        for area in [500, 500, 500]) / math.log(3)
        print("Expected entropy index for equal area:", expected)
        self.assertAlmostEqual(indices.entropy_index(), expected)

    def test_herfindahl_hirschman_index_single_land_use(self):
        land_use_areas = {
            "residential": 1000
        }
        indices = LandUseMixIndices(land_use_areas)
        expected = 10000.0
        print("Expected Herfindahl-Hirschman index for single land use:", expected)
        self.assertAlmostEqual(indices.herfindahl_hirschman_index(), expected)

    def test_herfindahl_hirschman_index_equal_area(self):
        land_use_areas = {
            "residential": 500,
            "commercial": 500,
            "industrial": 500
        }
        indices = LandUseMixIndices(land_use_areas)
        expected = sum((100 * (area / 1500)) ** 2 for area in [500, 500, 500])
        print("Expected Herfindahl-Hirschman index for equal area:", expected)
        self.assertAlmostEqual(indices.herfindahl_hirschman_index(), expected)


if __name__ == "__main__":
    unittest.main()
