# AeroRoutes
[![Build Status](https://app.travis-ci.com/javiergarciaheras/AeroRoutes.svg?branch=main)](https://www.travis-ci.com/javiergarciaheras/AeroRoutes)
[![GitHub](https://img.shields.io/github/license/javiergarciaheras/AeroRoutes)]()
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/javiergarciaheras/AeroRoutes)]()

## What is AeroRoutes?
AeroRoutes is a library to compute the main features in aircraft routes. Now it is supported loxodrome and orthodrome routes. The primary purpose is purely academic to show students their different characteristics.

## How to run the library

1. Clone or download the repository.
2. Install all the dependencies.


## How to use it

1. Create the latitude and longitude of both origin and destination. If you know only the coordinates in degrees, minutes and seconds you can use the function convert_dms_to_dec from aeroroutes.tools.

```python
# Madrid:
LEMD_lon = convert_dms_to_dec(3, 34, 2.47, 'W')
LEMD_lat = convert_dms_to_dec(40, 29, 37.62, 'N')
# Tokyo:
RJAA_lon = convert_dms_to_dec(140, 23, 17.66, 'E')
RJAA_lat = convert_dms_to_dec(35, 46, 24.78, 'N')
```

2. Create and instance to aeroroutes.routes.ComputeOrto or aeroroutes.routes.ComputeLoxo including origin and destination lon lat as a list, also de number of legs in your route could be also defined.

```python
# Orthodrome:
ortographic = ComputeOrto([LEMD_lon, LEMD_lat], [RJAA_lon, RJAA_lat], 100)

# Loxodrome
loxodromic = ComputeLoxo([LEMD_lon, LEMD_lat], [RJAA_lon, RJAA_lat], 100)

```

3. In previous object all features are already computed. You could obtain the following:

- Route with lons and lats along all segments.

```python
# Orthodrome:
lon_o, lat_o = ortographic.get_route()

# Loxodrome
lon_l, lat_l = loxodromic.get_route()

```

- Route distances in km.

```python
# Orthodrome:
d_o = ortographic.get_distance_km()

# Loxodrome
d_l = loxodromic.get_distance_km()

```

- Arc between point in the orthodrome route.

```python
# Orthodrome:
d_o = ortographic.get_arc_between_points()

```

- Geographic track in deg.

```python
# Orthodrome:
gamma_o = loxodromic.get_geographic_track()

```

4. Finally, routes can be plotted using different projections with the funciton from aeroroutes.tools.plot_routes. The library uses matplotlib basemap (([matplotlib basemap website](https://matplotlib.org/basemap/users/))). The lats and lons from the routes and the parameters for the Basemap (kwargs dictionary) are only needed. As you can see in the following examples:

- Plot using Mercator projection. ([matplotlib basemap website](https://matplotlib.org/basemap/users/merc.html)). Parallels, and meridians inputs are the values you want to see on the map, as a numpy array.

```python
kwargs = {"projection": 'merc', "llcrnrlat": 20, "urcrnrlat": 80, "llcrnrlon": -20,
                  "urcrnrlon": 150, "lat_ts": 20, "resolution": 'c'}

plot_routes(ortographic.lon_deg, ortographic.lat_deg,
                    parallels=np.arange(30., 91., 30.),
                    meridians=np.arange(-10., 181., 60.), **kwargs)

plot_routes(loxodromic.lon_deg, loxodromic.lat_deg,
                    parallels=np.arange(30., 91., 30.),
                    meridians=np.arange(-10., 181., 60.), **kwargs)



```

- Plot using Lamber Conformal projection. ([matplotlib basemap website](https://matplotlib.org/basemap/users/lcc.html)). Parallels, and meridians inputs are the values you want to see on the map, as a numpy array.

```python
kwargs = {"projection": 'lcc', "width": 12000000, "height": 9000000, "rsphere": (6378137.00, 6356752.3142),
                  "resolution": 'l', "area_thresh": 1000., "lat_1": 45, "lat_2": 55, "lat_0": 50, "lon_0": 80.}

plot_routes(ortographic.lon_deg, ortographic.lat_deg,
                    parallels=np.arange(30., 91., 30.),
                    meridians=np.arange(-10., 181., 60.), **kwargs)

plot_routes(loxodromic.lon_deg, loxodromic.lat_deg,
                    parallels=np.arange(30., 91., 30.),
                    meridians=np.arange(-10., 181., 60.), **kwargs)

```
