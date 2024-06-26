
import math


class LandUseMixIndices:
    def __init__(self, land_use_areas):
        self.land_use_areas = land_use_areas

    def entropy_index(self):
        total_area = sum(self.land_use_areas.values())
        k = len(self.land_use_areas)
        if k == 1:
            return 0
        entropy = -sum((area / total_area) * math.log(area / total_area)
                       for area in self.land_use_areas.values()) / math.log(k)
        return round(entropy, 2)

    def herfindahl_hirschman_index(self):
        total_area = sum(self.land_use_areas.values())
        hhi = sum((100 * (area / total_area)) **
                  2 for area in self.land_use_areas.values())
        return round(hhi, 2)
