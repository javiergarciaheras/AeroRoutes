from aeroroutes.tools import convert_dms_to_dec, plot_routes, convert2_spherical
from aeroroutes.constants import R_earth_km, d2r, r2d
import numpy as np


class ComputeOrto(object):
    def __init__(self, initial_wp, final_wp, num_legs=100):
        # x_p + B*y_p + C*z_p =0
        # x_q + B*y_q + C*z_q =0
        x_p, y_p, z_p = convert2_spherical(initial_wp[0], initial_wp[1])
        x_q, y_q, z_q = convert2_spherical(final_wp[0], final_wp[1])

        e = np.array([[y_p, z_p], [y_q, z_q]])
        f = - np.array([x_p, x_q])
        bc = np.linalg.inv(e) @ f
        b = bc[0]
        c = bc[1]

        # Also belong to the sphere:
        # x = R*cos(lat)*cos(lon)
        # y = R*con(lat)*sin(lon)
        # z = R*sing(lat)
        # Then lat as a function of lon is:
        # lat = atan2(-(cos(lon)+B*sin(lon)),C)
        self.lon_deg = np.linspace(initial_wp[0], final_wp[0], num_legs)
        self.lat_deg = np.arctan(-(np.cos(self.lon_deg * d2r) + (b * np.sin(self.lon_deg * d2r))) / c) * r2d

        # r_p · r_q = R^2*cos(theta) where theta is the angle of the arc between point P and Q
        theta_rad = np.arccos((x_p * x_q + y_p * y_q + z_p * z_q) / R_earth_km ** 2)
        self.theta_deg = theta_rad * r2d

        # d = R*theta
        self.d_km = R_earth_km * theta_rad

    def get_route(self):
        return self.lon_deg, self.lat_deg

    def get_arc_between_points(self):
        return self.theta_deg

    def get_distance_km(self):
        return self.d_km


class ComputeLoxo(object):
    def __init__(self, initial_wp, final_wp, num_legs=100):
        # the geographic track is constant and unknown
        gamma_rad = np.arctan((final_wp[0] - initial_wp[0]) * d2r / (
                    np.arctanh(np.sin(final_wp[1] * d2r)) - np.arctanh(np.sin(initial_wp[1] * d2r))))
        self.gamma_deg = gamma_rad * r2d

        self.lon_deg = np.linspace(initial_wp[0], final_wp[0], num_legs)
        self.lat_deg = np.arcsin(np.tanh(
            np.arctanh(np.sin(initial_wp[1] * d2r)) + (self.lon_deg * d2r - initial_wp[0] * d2r) / np.tan(
                gamma_rad))) * r2d

        self.d_km = (R_earth_km / np.cos(gamma_rad)) * np.abs((final_wp[1] * d2r) - (initial_wp[1] * d2r))

    def get_route(self):
        return self.lon_deg, self.lat_deg

    def get_geographic_track(self):
        return self.gamma_deg

    def get_distance_km(self):
        return self.d_km

