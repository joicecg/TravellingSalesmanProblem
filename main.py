import sys, math, random

from city import City
from genetic_algorithm import Genetic_Algorithm

def load_cities_from_file(path):
    file = open(path, "r")
    cities = []

    for line in file:
        city_data = line.split()
        id = city_data[0]
        x = city_data[1]
        y = city_data[2]

        cities.append(City(id, x, y))

    return cities

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
