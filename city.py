# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:53:35 2019

@author: I502765
"""
import math

class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def get_distance(self, other_city):
        distance_x = abs(float(self.x) - float(other_city.x)) ** 2
        distance_y = abs(float(self.y) - float(other_city.y)) ** 2

        return math.sqrt(distance_x + distance_y)

