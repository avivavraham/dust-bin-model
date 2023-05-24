# dust_bin.py
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
        self.sensors = []
        self.capacity = 0

    def __init__(self, width, length, height, sensors):
        """
        :param width: the width of the bin
        :param length: the length of the bin
        :param height: the height of the bin
        :param sensors: list of sensors
        """
        self.width = width
        self.length = length
        self.height = height
        self.sensors = sensors
        self.capacity = 0

    def calculate_trash_level(self):
        """
        :return: -1 if error accord. a capacity between 0 to 100 otherwise.
        """
        # Iterate through the sensors and retrieve sensors data which is 3 points, representing a plain.
        sensors_data = []
        for sensor in self.sensors:
            data = sensor.get_sensor_data()
            if 0 <= data <= self.height:
                sensors_data.append(self.height - data)
            else:
                return -1
        average_height = sum(sensors_data) / len(sensors_data)
        if average_height == 0:
            return 0
        else:
            return average_height / self.height * 100

    def get_capacity(self):
        self.capacity = int(100 - self.calculate_trash_level())
        return self.capacity

    def add_sensor(self, sensor):
        self.sensors.append(sensor)
