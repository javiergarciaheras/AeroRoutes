import unittest
import numpy as np
from aeroroutes.routes import ComputeOrto
from aeroroutes.tools import convert_dms_to_dec
from aeroroutes.tools import plot_routes


class TestOrtodromic2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # San Francisco:
        KSFO_lon = convert_dms_to_dec(122, 22, 31, 'W')
        KSFO_lat = convert_dms_to_dec(37, 37, 8, 'N')
        # Madrid:
        LEMD_lon = convert_dms_to_dec(3, 33, 39, 'W')
        LEMD_lat = convert_dms_to_dec(40, 28, 20, 'N')

        cls.ortographic = ComputeOrto([KSFO_lon, KSFO_lat], [LEMD_lon, LEMD_lat], 100)

    def test_route(self):
        lons, lats = self.ortographic.get_route()
        self.assertEqual(len(lons), 100, 'longitude length is not right')
        self.assertEqual(lons[50], -62.36798260381593, 'longitude index 50 is not right')
        self.assertEqual(len(lats), 100, 'latitude length is not right')
        self.assertEqual(lats[50], 57.9266350464969, 'latitude index 50 is not right')
        self.assertEqual(np.sum(lons), -6296.805555555556, 'Sum longitudes is not right')
        self.assertEqual(round(np.sum(lats), 10), 5220.7900179244, 'Sum latitudes is not right')

    def test_distance(self):
        distance = self.ortographic.get_distance_km()
        self.assertEqual(distance, 9332.327459405758, 'Orthodrome distance is not right')

    def test_arc_between_points(self):
        theta = self.ortographic.get_arc_between_points()
        self.assertEqual(theta, 83.92763717752254, 'Orthodrome arc between points is not right')

    def test_get_latitude(self):
        lat = self.ortographic.get_latitude(-50)
        self.assertEqual(lat, 57.42977387337658, 'Orthodrome latitude at W50 is not right')


    def test_plot_Lamber_Conformal(self):
        # Lambert Conformal Projection
        # ============================
        # setup lambert conformal basemap.
        # lat_1 is first standard parallel.
        # lat_2 is second standard parallel (defaults to lat_1).
        # lon_0,lat_0 is central point.
        # rsphere=(6378137.00,6356752.3142) specifies WGS84 ellipsoid
        # area_thresh=1000 means don't plot coastline features less
        # than 1000 km^2 in area.
        kwargs = {"projection": 'lcc', "width": 12000000, "height": 9000000, "rsphere": (6378137.00, 6356752.3142),
                  "resolution": 'l', "area_thresh": 1000., "lat_1": 45, "lat_2": 55, "lat_0": 50, "lon_0": -50.}
        plot_routes(self.ortographic.lon_deg, self.ortographic.lat_deg,
                    parallels=np.arange(30., 91., 30.),
                    meridians=np.arange(-120., 1., 60.), **kwargs)

if __name__ == '__main__':
    unittest.main()
