# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:06:03 2019

@author: I502765
"""

import sys, math, random, heapq
import matplotlib.pyplot as plt
from itertools import chain

#if sys.version_info < (3, 0):
#   sys.exit("""Sorry, requires Python 3.x, not Python 2.x.""")

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.n = len(vertices)

    # Lookup table for distances
    _d_lookup = {}

    def d(self, u, v):
        """Euclidean Metric d_2((x1, y1), (x2, y2))"""

        # Check if the distance was computed before
        if (u, v) in self._d_lookup:
            return self._d_lookup[(u, v)]

        # Otherwise compute it
        _distance = math.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)

        # Add to dictionary
        self._d_lookup[(u, v)], self._d_lookup[(v, u)] = _distance, _distance
        return _distance

    def plot(self, tour=None):
        """Plots the cities and superimposes given tour"""

        if tour is None:
            tour = Tour(self, [])

        _vertices = [self.vertices[0]]

        for i in tour.vertices:
            _vertices.append(self.vertices[i])

        _vertices.append(self.vertices[0])

        plt.title("Cost = " + str(tour.cost()))
        plt.plot(*zip(*_vertices), '-r')
        plt.scatter(*zip(*self.vertices), c="b", s=10, marker="s")
        plt.show()


class Tour:

    def __init__(self, g, vertices = None):
        """Generate random tour in given graph g"""

        self.g = g

        if vertices is None:
            self.vertices = list(range(1, g.n))
            random.shuffle(self.vertices)
        else:
            self.vertices = vertices

        self.__cost = None

    def get_cost(self):
        return self.__cost


    def cost(self):
        """Return total edge-cost of tour"""
        if self.__cost is None:
            pts = [self.g.vertices[i] for i in self.vertices]
            pts.append(self.g.vertices[0])
            self.__cost = sum(map(g.d, pts, pts[1:])) + g.d(pts[0], pts[-1])
        return self.__cost

class GeneticAlgorithm:

    def __init__(self, g, population_size, k=5, elite_mating_rate=0.5,
                 mutation_rate=0.015, mutation_swap_rate=0.2):
        """Initialises algorithm parameters"""

        self.g = g

        self.population = []
        for _ in range(population_size):
            self.population.append(Tour(g))

        self.population_size = population_size
        self.k = k
        self.elite_mating_rate = elite_mating_rate
        self.mutation_rate = mutation_rate
        self.mutation_swap_rate = mutation_swap_rate

    def crossover(self, mum, dad):
        """Implements ordered crossover"""

        size = g.n - 1

        # Choose random start/end position for crossover
        start, end = sorted([random.randrange(size) for _ in range(2)])

        # Identify the elements from mum's sequence which end up in alice,
        # and from dad's which end up in bob    
        mumxo = set(mum.vertices[start:end+1])
        dadxo = set(dad.vertices[start:end+1])

        # Take the other elements in their original order
        alice = [i for i in dad.vertices if not i in mumxo]
        bob = [i for i in mum.vertices if not i in dadxo]

        # Insert selected elements of mum's sequence for alice, dad's for bob
        alice[start:start] = mum.vertices[start:end+1]
        bob[start:start] = dad.vertices[start:end+1]

        # Return twins
        return Tour(self.g, alice), Tour(self.g, bob)

    def mutate(self, tour):
        """Randomly swaps pairs of cities in a given tour according to mutation rate"""
        n = len(tour.vertices)
        # Decide whether to mutate
        if random.random() < self.mutation_rate:

            # For each vertex
            for i in range(n):

                # Randomly decide whether to swap
                if random.random() < self.mutation_swap_rate:

                    # Randomly choose other city position
                    j = random.randrange(len(tour.vertices))

                    # Swap
                    tour.vertices[i], tour.vertices[j] = tour.vertices[j], tour.vertices[i]

    def select_parent(self, k):
        """Implements k-tournament selection to choose parents"""
        tournament = random.sample(self.population, k)
        return max(tournament, key=lambda t: t.cost())

    def evolve(self):
        """Executes one iteration of the genetic algorithm to obtain a new generation"""

        new_population = []

        for _ in range(self.population_size):

            # K-tournament for parents
            mum, dad = self.select_parent(self.k), self.select_parent(self.k)
            alice, bob = self.crossover(mum, dad)

            # Mate in an elite fashion according to the elitism_rate
            if random.random() < self.elite_mating_rate:
                if alice.cost() < mum.cost() or alice.cost() < dad.cost():
                    new_population.append(alice)
                if bob.cost() < mum.cost() or bob.cost() < dad.cost():
                    new_population.append(bob)

            else:
                self.mutate(alice)
                self.mutate(bob)
                new_population += [alice, bob]

        # Add new population to old
        self.population += new_population

        # Retain fittest
        self.population = sorted(self.population, key=lambda t: t.cost())[0:self.population_size]


    def run(self, iterations=5000):
        for _ in range(iterations):
            self.evolve()

    def best(self):
        return max(self.population, key=lambda t: t.cost())

sys.argv.append('input/berlin52.tsp.txt')
sys.argv.append(5)
file = open(sys.argv[1], "r")
lines = file.readlines()
vertices = []
for line in lines:
    l = line.split()
    x = float(l[1])
    y = float(l[2])
    vertices.append((x, y))

g = Graph(vertices)

ga = GeneticAlgorithm(g, sys.argv[2])
ga.run()

best_tour = ga.best()
print(best_tour.get_cost())
g.plot(best_tour)

   
