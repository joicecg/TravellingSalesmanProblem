class Route:
    def __init__(self, cities):
        self.cities = cities
        self.distance = self.calculate_distance()
        self.fitness = self.calculate_fitness()

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def calculate_distance(self):
        path_distance = 0

        for i in range(0, len(self.cities)):
            from_city = self.cities[i]
            to_city = None
            if i + 1 < len(self.cities):
                to_city = self.cities[i + 1]
            else:
                to_city = self.cities[0]
            path_distance += from_city.get_distance(to_city)

        return path_distance

    def calculate_fitness(self):
        return 1 / float(self.distance)
