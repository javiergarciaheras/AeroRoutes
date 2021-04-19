import unittest
import numpy as np
from aeroroutes.routes import ComputeOrto
from aeroroutes.tools import convert_dms_to_dec, plot_routes


class TestOrtodromic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Madrid:
        LEMD_lon = convert_dms_to_dec(3, 34, 2.47, 'W')
        LEMD_lat = convert_dms_to_dec(40, 29, 37.62, 'N')
        # Tokyo:
        RJAA_lon = convert_dms_to_dec(140, 23, 17.66, 'E')
        RJAA_lat = convert_dms_to_dec(35, 46, 24.78, 'N')

        cls.ortographic = ComputeOrto([LEMD_lon, LEMD_lat], [RJAA_lon, RJAA_lat], 100)

    def test_plot_mercator(self):
        # https://matplotlib.org/basemap/users/
        # plot on Mercator
        # =================
        # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
        # are the lat/lon values of the lower left and upper right corners
        # of the map.
        # lat_ts is the latitude of true scale.
        # resolution = 'c' means use crude resolution coastlines.
        kwargs = {"projection": 'merc', "llcrnrlat": 20, "urcrnrlat": 80, "llcrnrlon": -20,
                  "urcrnrlon": 150, "lat_ts": 20, "resolution": 'c'}
        plot_routes(self.ortographic.lon_deg, self.ortographic.lat_deg,
                    parallels=np.arange(30., 91., 30.),
                    meridians=np.arange(-10., 181., 60.), **kwargs)

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
                  "resolution": 'l', "area_thresh": 1000., "lat_1": 45, "lat_2": 55, "lat_0": 50, "lon_0": 80.}
        plot_routes(self.ortographic.lon_deg, self.ortographic.lat_deg,
                    parallels=np.arange(30., 91., 30.),
                    meridians=np.arange(-10., 181., 60.), **kwargs)



if __name__ == '__main__':
    unittest.main()
