import math
import matplotlib.pyplot as plot

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.n = len(vertices)

    _distances = {}

    def distance(self, f_city, s_city):
        if (f_city, s_city) in self._distances:
            return self._distances[(f_city, s_city)]
        
        x_distance = (f_city[0] - s_city[0]) ** 2
        y_distance = (f_city[1] - s_city[1]) ** 2
        _distance = math.sqrt( x_distance + y_distance ) 

        self._distances[(f_city, s_city)], self._distances[(s_city, f_city)] = _distance, _distance
        return _distance

    def plot(self, route=None):

        _vertices = [self.vertices[0]]

        for i in route.vertices:
            _vertices.append(self.vertices[i])

        _vertices.append(self.vertices[0])

        plot.title("Cost = " + str(route.route_cost()))
        plot.plot(*zip(*_vertices), '-r')
        plot.scatter(*zip(*self.vertices), c="b", s=10, marker="s")
        plot.show()