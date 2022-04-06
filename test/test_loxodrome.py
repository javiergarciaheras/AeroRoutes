import unittest
import numpy as np
from aeroroutes.routes import ComputeLoxo
from aeroroutes.tools import convert_dms_to_dec


class TestLoxodromic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Madrid:
        LEMD_lon = convert_dms_to_dec(3, 34, 2.47, 'W')
        LEMD_lat = convert_dms_to_dec(40, 29, 37.62, 'N')
        # Tokyo:
        RJAA_lon = convert_dms_to_dec(140, 23, 17.66, 'E')
        RJAA_lat = convert_dms_to_dec(35, 46, 24.78, 'N')

        cls.loxodromic = ComputeLoxo([LEMD_lon, LEMD_lat], [RJAA_lon, RJAA_lat], 100)

    def test_route(self):
        lons, lats = self.loxodromic.get_route()
        self.assertEqual(len(lons), 100, 'longitude length is not right')
        self.assertEqual(lons[50], 69.1374914983165, 'longitude index 50 is not right')
        self.assertEqual(len(lats), 100, 'latitude length is not right')
        self.assertEqual(round(lats[50], 10), 38.1480178817, 'latitude index 50 is not right')
        self.assertEqual(np.sum(lons), 6841.044305555556, 'Sum longitudes is not right')
        self.assertEqual(np.sum(lats), 3815.8871159935607, 'Sum latitudes is not right')

    def test_distance(self):
        distance = self.loxodromic.get_distance_km()
        self.assertEqual(distance, 12593.754742038487, 'Loxodrome distance is not right')

    def test_arc_between_points(self):
        gamma = self.loxodromic.get_geographic_track()
        self.assertEqual(gamma, -87.61140980228046, 'Loxodrome geographic track is not right')


if __name__ == '__main__':
    unittest.main()
