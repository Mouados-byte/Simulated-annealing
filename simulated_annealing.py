import math
import random


class simulated_annealing:
    def __init__(self, problem, max_iter=1000, t0=1.0, alpha=0.99):
        self.problem = problem
        self.max_iter = max_iter
        self.t0 = t0
        self.alpha = alpha
        self.progress = []
        self.states = []

    def solve(self):
        t = self.t0
        current = self.problem.initial()
        current_cost = self.problem.cost(current)
        best = current
        best_cost = current_cost
        self.progress.append(current_cost)
        self.states.append(current[:])
        for i in range(self.max_iter):
            next = self.problem.neighbor(current)
            next_cost = self.problem.cost(next)
            delta = next_cost - current_cost
            if delta < 0 or random.random() < self.probability(current_cost, next_cost, t):
                current = next
                current_cost = next_cost
                if next_cost < best_cost:
                    best = next
                    best_cost = next_cost
            t = t * self.alpha
            self.progress.append(current_cost)
            self.states.append(current[:])
        return best, best_cost
      
    def probability(self, current_cost, next_cost, t):
        return math.exp(-(next_cost - current_cost) / t)
    
