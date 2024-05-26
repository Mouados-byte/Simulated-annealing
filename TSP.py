# TSP (Traveling Salesman Problem) is a classic optimization problem. 
# The goal is to find the shortest path that visits all cities exactly once and returns to the starting city. 
# The problem is defined by a list of cities and a matrix of distances between them. 
# The simulated_annealing class implements the simulated annealing algorithm to solve the TSP. 
import math
import random
from problem import Problem
from simulated_annealing import simulated_annealing

class TSP(Problem):
    def __init__(self, cities, dists):
        self.cities = cities
        self.dists = dists

    def initial(self):
        return random.sample(self.cities, len(self.cities))

    def cost(self, state):
        c = 0
        for i in range(len(self.cities)):
            c += self.dists[i][(i + 1) % len(self.cities)]
        return c
      
    def cost(self, state):
      c = 0
      for i in range(len(self.cities)):
          c += self.dists[self.cities.index(state[i])][self.cities.index(state[(i + 1) % len(self.cities)])]
      return c

    def neighbor(self, state):
        [a, b] = random.sample(range(len(self.cities)), 2)
        state[a], state[b] = state[b], state[a]
        return state
    
    def solve(self):
      sa = simulated_annealing(self)
      return sa.solve()
      