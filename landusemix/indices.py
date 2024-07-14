"""
This module contains a class that calculates land use mix indices.
"""
import math

class LandUseMixIndices:
    """
    A class that calculates land use mix indices.

    Attributes:
        land_use_areas (dict): A dictionary containing land use areas.

    Methods:
        entropy_index: Calculates the entropy index.
        herfindahl_hirschman_index: Calculates the Herfindahl-Hirschman index.
    """

    def __init__(self, land_use_areas):
        """
        Initializes a LandUseMixIndices object.

        Args:
            land_use_areas (dict): A dictionary containing land use areas.
        """
        self.land_use_areas = land_use_areas

    def entropy_index(self):
        """
        Calculates the entropy index.

        Returns:
            float: The entropy index value.
        """
        total_area = sum(self.land_use_areas.values())
        k = len(self.land_use_areas)
        if k == 1:
            return 0
        entropy = -sum((area / total_area) * math.log(area / total_area)
                       for area in self.land_use_areas.values()) / math.log(k)
        return round(entropy, 2)

    def herfindahl_hirschman_index(self):
        """
        Calculates the Herfindahl-Hirschman index.

        Returns:
            float: The Herfindahl-Hirschman index value.
        """
        total_area = sum(self.land_use_areas.values())
        hhi = sum((100 * (area / total_area)) **
                  2 for area in self.land_use_areas.values())
        return round(hhi, 2)
