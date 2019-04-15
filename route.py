import random

class Route:
    def __init__(self, city_graph, vertices = None):
        self.city_graph = city_graph
        self.__cost = None
        
        if vertices is None:
            self.vertices = list(range(1, city_graph.n))
            random.shuffle(self.vertices)
        else:
            self.vertices = vertices


    def get_cost(self):
        return self.__cost

    def route_cost(self):
        if self.__cost is None:
            pts = [self.city_graph.vertices[i] for i in self.vertices]
            pts.append(self.city_graph.vertices[0])
            self.__cost = sum(map(self.city_graph.distance, pts, pts[1:])) + self.city_graph.distance(pts[0], pts[-1])
        return self.__cost
