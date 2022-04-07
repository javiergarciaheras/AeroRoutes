import unittest
import numpy as np
from aeroroutes.routes import ComputeLoxo
from aeroroutes.tools import convert_dms_to_dec
from aeroroutes.tools import plot_routes

class TestLoxodromic2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # San Francisco:
        KSFO_lon = convert_dms_to_dec(122, 22, 31, 'W')
        KSFO_lat = convert_dms_to_dec(37, 37, 8, 'N')
        # Madrid:
        LEMD_lon = convert_dms_to_dec(3, 33, 39, 'W')
        LEMD_lat = convert_dms_to_dec(40, 28, 20, 'N')


        cls.loxodromic = ComputeLoxo([KSFO_lon, KSFO_lat], [LEMD_lon, LEMD_lat], 100)

    def test_route(self):
        lons, lats = self.loxodromic.get_route()
        self.assertEqual(len(lons), 100, 'longitude length is not right')
        self.assertEqual(lons[50], -62.36798260381593, 'longitude index 50 is not right')
        self.assertEqual(len(lats), 100, 'latitude length is not right')
        self.assertEqual(round(lats[50], 10), 39.0743773611, 'latitude index 50 is not right')
        self.assertEqual(np.sum(lons), -6296.805555555556, 'Sum longitudes is not right')
        self.assertEqual(np.sum(lats), 3905.506607398399, 'Sum latitudes is not right')

    def test_distance(self):
        distance = self.loxodromic.get_distance_km()
        self.assertEqual(distance, 10263.148676129978, 'Loxodrome distance is not right')

    def test_arc_between_points(self):
        gamma = self.loxodromic.get_geographic_track()
        self.assertEqual(gamma, 88.22846925638366, 'Loxodrome geographic track is not right')

    def test_get_latitude(self):
        lat = self.loxodromic.get_latitude(-50)
        self.assertEqual(lat, 39.37071946912703, 'Loxodrome latitude at W50 is not right')

    def test_plot_mercator(self):
        # https://matplotlib.org/basemap/users/
        # plot on Mercator
        # =================
        # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
        # are the lat/lon values of the lower left and upper right corners
        # of the map.
        # lat_ts is the latitude of true scale.
        # resolution = 'c' means use crude resolution coastlines.
        kwargs = {"projection": 'merc', "llcrnrlat": 20, "urcrnrlat": 80, "llcrnrlon": -130,
                  "urcrnrlon": 0, "lat_ts": 20, "resolution": 'c'}
        plot_routes(self.loxodromic.lon_deg, self.loxodromic.lat_deg,
                    parallels=np.arange(30., 91., 30.),
                    meridians=np.arange(-120., 1., 60.), **kwargs)

if __name__ == '__main__':
    unittest.main()
