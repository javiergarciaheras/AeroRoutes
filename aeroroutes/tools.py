import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from aeroroutes.constants import R_earth_km, d2r, r2d
import numpy as np


def convert_dms_to_dec(dd, mm, ss, nswe):
    """

    :rtype: float
    """
    if nswe == 'N' or nswe == 'E':
        decimal_deg = dd + mm/60.0 + ss/3600.0
    else:
        decimal_deg = -(dd + mm / 60.0 + ss / 3600.0)

    return decimal_deg


def plot_routes(lons, lats, parallels=np.arange(30., 91., 30.),
                meridians=np.arange(-10., 181., 60.), **kwargs):
    # https://matplotlib.org/basemap/api/basemap_api.html

    m = Basemap(**kwargs)
    m.drawcoastlines()
    #m.fillcontinents(color='coral', lake_color='aqua')
    # draw parallels and meridians.
    m.drawparallels(parallels)
    m.drawmeridians(meridians)
    #m.drawmapboundary(fill_color='aqua')
    x, y = m(lons, lats)

    m.plot(x, y, marker=None, color='b')

    plt.show()


def convert2_spherical(lon_deg, lat_deg):
    x = R_earth_km * np.cos(lat_deg * d2r) * np.cos(lon_deg * d2r)
    y = R_earth_km * np.cos(lat_deg * d2r) * np.sin(lon_deg * d2r)
    z = R_earth_km * np.sin(lat_deg * d2r)
    return x, y, z

