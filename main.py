import sys
from graph import Graph
from genetic_algorithm import Genetic_Algorithm

def load_cities_from_file(path):
    file = open(path, "r")
    lines = file.readlines()
    vertices = []
    for line in lines:
        l = line.split()
        x = float(l[1])
        y = float(l[2])
        vertices.append((x, y))
    
    return Graph(vertices)

class __main__:
    # sys.argv.append('input/berlin52.tsp.txt')
 #   sys.argv.append('input/pr76.tsp.txt')
    sys.argv.append('input/st70.tsp.txt')
    
    population = 1000
    iterations = 500
    
    city_graph = load_cities_from_file('input/st70.tsp.txt')
    
    ga = Genetic_Algorithm(city_graph, population)
    ga.run(iterations)
    
    best_route = ga.best()
    print(best_route.get_cost())
    city_graph.plot(best_route)