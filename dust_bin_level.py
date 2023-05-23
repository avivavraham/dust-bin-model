# dust_bin_level.py
import numpy as np


class DustBinLevel:
    def __init__(self):
        self.level = 0.0

    def set_level(self, level):
        self.level = level

    def get_level(self):
        return self.level
