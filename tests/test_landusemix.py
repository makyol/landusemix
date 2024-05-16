
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
        self.assertAlmostEqual(self.indices.entropy_index(), expected)

    def test_herfindahl_hirschman_index(self):
        expected = sum((100 * (area / 1000)) ** 2 for area in [500, 300, 200])
        self.assertAlmostEqual(self.indices.herfindahl_hirschman_index(), expected)

if __name__ == "__main__":
    unittest.main()
