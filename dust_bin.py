# dust_bin.py
import numpy as np
from sympy import Plane, Point3D
import math
from dust_bin_level import DustBinLevel
from dust_bin_sensor import Sensor


class DustBin:
    def __init__(self, width, length, height):
        """
        :param width: the width of the bin
        :param length: the length of the bin
        :param height: the height of the bin
        """
        self.width = width
        self.length = length
        self.height = height
        self.level = DustBinLevel()
        self.sensors = []
        self.volume = width * length * height

    def calculate_trash_level(self):
        """
        :return: -1 if error accord. a number between 0 to 100 otherwise.
        """
        # Iterate through the sensors and retrieve sensors data which is 3 points, representing a plain.
        sensors_data = []
        for sensor in self.sensors:
            data = sensor.get_sensor_data()
            point = sensor.get_sensor_info()[2]
            if 0 <= data <= self.height:
                point.append(self.height - data)
            else:
                return -1
            sensors_data.append(point)
        # Calculate the plane equation using p1, p2, and p3
        plane = Plane(Point3D(*sensors_data[0]), Point3D(*sensors_data[1]), Point3D(*sensors_data[2]))
        a, b, c, d = plane.normal_vector.args  # Extract the coefficients of the plane equation
        intersection_polygon = self.calculate_intersection_polygon(plane)
        intersection_volume = self.calculate_polygon_volume(intersection_polygon)

        # Update the remaining capacity based on the intersection volume
        remaining_capacity -= intersection_volume

        # Implement trash level calculation logic here
        # Update the dust bin level using self.level.set_level(level)
        pass

    def calculate_intersection_polygon(self, plane):
        intersection_points = []

        # Calculate intersection points of the plane with the bin's edges or faces
        # You'll need to implement this logic based on the specifics of your bin's shape

        return intersection_points

    def calculate_polygon_volume(self, polygon):
        # Calculate the volume of the polygon using the height of the bin
        # Assuming polygon is a list of 2D points (x, y) representing the polygon's vertices
        # You can use various methods to calculate the volume based on the polygon's shape

        if len(polygon) < 3:
            return 0.0  # Invalid polygon, no volume

        # Calculate the signed area of the polygon
        signed_area = 0.0
        for i in range(len(polygon)):
            x1, y1 = polygon[i]
            x2, y2 = polygon[(i + 1) % len(polygon)]
            signed_area += (x1 * y2 - x2 * y1)
        signed_area /= 2.0

        # Calculate the volume based on the signed area and the bin's height
        volume = abs(signed_area) * self.height

        return volume

    def add_sensor(self, sensor):
        self.sensors.append(sensor)
