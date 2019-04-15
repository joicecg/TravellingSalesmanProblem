import random

from route import Route

class Genetic_Algorithm:
    def __init__(self, city_graph, population_size, k=5, elite_mating_rate=0.5,
                 mutation_rate=0.015, mutation_swap_rate=0.2):
        self.city_graph = city_graph
        self.population = []
        
        for _ in range(population_size):
            self.population.append(Route(city_graph))

        self.population_size = population_size
        self.k = k
        self.elite_mating_rate = elite_mating_rate
        self.mutation_rate = mutation_rate
        self.mutation_swap_rate = mutation_swap_rate

    def crossover(self, mom, dad):
        size = self.city_graph.n - 1
        start, end = sorted([random.randrange(size) for _ in range(2)])

        momxo = set(mom.vertices[start:end+1])
        dadxo = set(dad.vertices[start:end+1])

        alice = [i for i in dad.vertices if not i in momxo]
        bob = [i for i in mom.vertices if not i in dadxo]

        alice[start:start] = mom.vertices[start:end+1]
        bob[start:start] = dad.vertices[start:end+1]

        return Route(self.city_graph, alice), Route(self.city_graph, bob)

    def mutate(self, route):
        n = len(route.vertices)
        
        if random.random() < self.mutation_rate:
            for i in range(n):
                if random.random() < self.mutation_swap_rate:
                    j = random.randrange(len(route.vertices))
                    route.vertices[i], route.vertices[j] = route.vertices[j], route.vertices[i]

    def select_parent(self, k):
        tournament = random.sample(self.population, k)
        return max(tournament, key=lambda route: route.route_cost())

    def evolve(self):
        new_population = []

        for _ in range(self.population_size):
            mom, dad = self.select_parent(self.k), self.select_parent(self.k)
            alice, bob = self.crossover(mom, dad)

            if random.random() < self.elite_mating_rate:
                if alice.route_cost() < mom.route_cost() or alice.route_cost() < dad.route_cost():
                    new_population.append(alice)
                if bob.route_cost() < mom.route_cost() or bob.route_cost() < dad.route_cost():
                    new_population.append(bob)

            else:
                self.mutate(alice)
                self.mutate(bob)
                new_population += [alice, bob]

        self.population += new_population

        self.population = sorted(self.population, key=lambda route: route.route_cost())[0:self.population_size]


    def run(self, iterations):
        for _ in range(iterations):
            self.evolve()

    def best(self):
        return max(self.population, key=lambda t: t.route_cost())
