from dust_bin_sensor import Sensor
from dust_bin import DustBin

sensor1 = Sensor("sensor 1", (10, 10, 50))
sensor2 = Sensor("sensor 2", (20, 20, 50))
sensor3 = Sensor("sensor 3", (30, 30, 50))
sensors = [sensor1, sensor2, sensor3]
Bin = DustBin(40, 40, 100, sensors)
print(Bin.get_capacity())
