import unittest
import numpy as np
from aeroroutes.routes import ComputeOrto
from aeroroutes.tools import convert_dms_to_dec


class TestOrthodrome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Madrid:
        LEMD_lon = convert_dms_to_dec(3, 34, 2.47, 'W')
        LEMD_lat = convert_dms_to_dec(40, 29, 37.62, 'N')
        # Tokyo:
        RJAA_lon = convert_dms_to_dec(140, 23, 17.66, 'E')
        RJAA_lat = convert_dms_to_dec(35, 46, 24.78, 'N')

        cls.orthodrome = ComputeOrto([LEMD_lon, LEMD_lat], [RJAA_lon, RJAA_lat], 100)

    def test_route(self):
        lons, lats = self.orthodrome.get_route()
        self.assertEqual(len(lons), 100, 'longitude length is not right')
        self.assertEqual(lons[50], 69.1374914983165, 'longitude index 50 is not right')
        self.assertEqual(len(lats), 100, 'latitude length is not right')
        self.assertEqual(lats[50], 68.5359501601219, 'latitude index 50 is not right')
        self.assertEqual(np.sum(lons), 6841.044305555556, 'Sum longitudes is not right')
        self.assertEqual(round(np.sum(lats), 10), 6062.1670594076, 'Sum latitudes is not right')

    def test_distance(self):
        distance = self.orthodrome.get_distance_km()
        self.assertEqual(distance, 10769.25292674978, 'Orthodrome distance is not right')

    def test_arc_between_points(self):
        theta = self.orthodrome.get_arc_between_points()
        self.assertEqual(theta, 96.850218366296, 'Orthodrome arc between points is not right')


if __name__ == '__main__':
    unittest.main()
