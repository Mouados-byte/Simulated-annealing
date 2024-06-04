import math
import random

class simulated_annealing:
    def __init__(self, problem, max_iter=1000, t0=1.0, alpha=0.99):
        # Initialisation des paramètres
        self.problem = problem
        self.max_iter = max_iter
        self.t0 = t0
        self.alpha = alpha
        self.progress = []
        self.states = []

    def solve(self):
        # Température initiale
        t = self.t0
        # État initial
        current = self.problem.initial()
        # Coût de l'état initial
        current_cost = self.problem.cost(current)
        # Meilleur état trouvé
        best = current
        # Coût du meilleur état trouvé
        best_cost = current_cost
        # Enregistrer le coût initial
        self.progress.append(current_cost)
        # Enregistrer l'état initial
        self.states.append(current[:])
        for i in range(self.max_iter):
            # Générer un voisin
            next = self.problem.neighbor(current)
            # Coût du voisin
            next_cost = self.problem.cost(next)
            # Différence de coût entre l'état courant et le voisin
            delta = next_cost - current_cost
            # Accepter le voisin si son coût est inférieur ou avec une certaine probabilité
            if delta < 0 or random.random() < self.probability(current_cost, next_cost, t):
                current = next
                current_cost = next_cost
                # Mettre à jour le meilleur état trouvé
                if next_cost < best_cost:
                    best = next
                    best_cost = next_cost
            # Diminuer la température
            t = t * self.alpha
            # Enregistrer le coût courant
            self.progress.append(current_cost)
            # Enregistrer l'état courant
            self.states.append(current[:])
        # Retourner le meilleur état et son coût
        return best, best_cost
      
    def probability(self, current_cost, next_cost, t):
        # Calculer la probabilité d'acceptation du voisin
        return math.exp(-(next_cost - current_cost) / t)
