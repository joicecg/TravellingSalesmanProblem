import sys, math, random

from city import City
from genetic_algorithm import Genetic_Algorithm

def load_cities_from_file(path):
    file = open(path, "r")
    lines = file.readlines()

    vertices = []
    for line in lines:
        l = line.split()
        vertices.append((l[1], l[2]))

    return City(vertices)

class __main__:
    # default file
    sys.argv.append('input/berlin52.tsp.txt')
    cities = load_cities_from_file(sys.argv[1])
    genetic_algorithm = Genetic_Algorithm(cities)
    genetic_algorithm.initialization(4)

    #TODO repeat until population has converged
    genetic_algorithm.selection()
    genetic_algorithm.crossover()
    #TODO mutation
    #TODO compute fitness
