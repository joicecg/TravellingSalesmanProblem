# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:53:35 2019

@author: I502765
"""
import math, random

cities_list = []
city_list_id = []

class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    
    def getDistance (self, otherCity):
        distanceX = abs(self.x - otherCity.x) ** 2
        distanceY = abs(self.y - otherCity.y) ** 2
        
        return math.sqrt(distanceX + distanceY)
        

    def getCities():
        arq = open("TSP/berlin52.tsp.txt", "r")
    
        for line in arq:
            city_data = line.split()
            city = City(city_data[0], city_data[1], city_data[2])
            city_list_id.append(city_data[0])
            cities_list.append(city)
        return cities_list
        
    def getCityById(id):
        return cities_list[id]
    
    def createRoute(cities_list):
        route = random.sample(city_list_id, len(city_list_id))
        print(route)
        return route
    
    def initialPopulation(popSize, cityList):
        population = []
    
        for i in range(0, popSize):
            population.append(City.createRoute(city_list_id))
        return population

class __main__:
    list = City.getCities()
    route = City.createRoute(list)
    City.initialPopulation(4, list)
