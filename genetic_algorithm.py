import sys, math, random

from city import City
from route import Route

class Genetic_Algorithm:
    def __init__(self, cities):
        self.cities = cities
        self.routes = []
        self.pairs_of_routes = []

    def initialization(self, size):
        for i in range(0, size):
            self.routes.append(Route(random.sample(self.cities, len(self.cities))))

    #TODO verifica isso aqui, funciona mas nao sei se realmente eh isso
    def selection(self):
        it = iter(sorted(self.routes))
        for route in it:
            temp = [] 
            temp.append(route)
            next(it)
            temp.append(route)
            self.pairs_of_routes.append(temp)

    def crossover(self):
        #TODO order 1 crossover
        for pairs in self.pairs_of_routes:
            print(pairs)
