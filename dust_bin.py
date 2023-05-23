# dust_bin.py
import numpy as np
from dust_bin_level import DustBinLevel


class DustBin:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.level = DustBinLevel()
        self.sensors = []

    def calculate_trash_level(self):
        # Iterate through the sensors and retrieve sensor data
        sensor_data = []
        for sensor in self.sensors:
            data = sensor.get_sensor_data()
            sensor_data.append(data)

        # Implement trash level calculation logic here
        # Update the dust bin level using self.level.set_level(level)
        pass
