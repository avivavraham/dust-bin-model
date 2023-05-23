import numpy as np


class Sensor:
    def __init__(self, name, location, angle):
        self.name = name
        self.location = location
        angle = np.radians(angle)  # Constant angle in radians at which the sensors are facing down

    def get_sensor_data(self):
        # Implement logic to retrieve sensor data here
        pass
