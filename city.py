# -*- coding: utf-8 -*-
import math

class Vertice:
    def __init__(self, x, y):
        self.x = x
        self.y = y   

class City:    
    def __init__(self, vertices):
        self.vertices = vertices
        self.vertices_quant = len(vertices)

    def get_x(self, vertice_id):
        return self.vertices[vertice_id][0]

    def get_y(self, vertice_id):
        return self.vertices[vertice_id][1]
        
    _distances = {}

    def get_distance(self, f_city, s_city):
        if (f_city, s_city) in self._distances:
            return self._distances[(f_city, s_city)]

        distance_x = abs(float(f_city.get_x) - float(s_city.get_x)) ** 2
        distance_y = abs(float(f_city.get_y) - float(s_city.get_y)) ** 2
        _distance = math.sqrt(distance_x + distance_y)
        print(_distance)

        self._distances[(f_city, s_city)], self._distances[(s_city, f_city)] = _distance, _distance
        return _distance

