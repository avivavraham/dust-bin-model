import numpy as np


class Sensor:
    def __init__(self, name, location, angle=90):
        """

        :param name: name of sensor
        :param location: a list [x,y] assuming the sensor is on the cover
        :param angle: angle of sensor in relation to the horizon. default is 90.
        """
        self.name = name
        self.location = location
        self.angle = np.radians(angle)  # Constant angle in radians at which the sensors are facing down

    def get_sensor_info(self):
        # Implement logic to retrieve sensor data here
        """
        :return: a tuple (name, location, angle)
        """
        return self.name, self.location, self.angle

    def get_sensor_data(self):
        # Implement logic to retrieve sensor data here
        """
        :return: distance to the closest point to the sensor
        """
        return 10
