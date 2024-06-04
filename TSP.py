# Le problème du voyageur de commerce (TSP) est un problème d'optimisation classique.
# L'objectif est de trouver le chemin le plus court qui visite toutes les villes exactement une fois et retourne à la ville de départ.
# Le problème est défini par une liste de villes et une matrice de distances entre elles.
# La classe simulated_annealing implémente l'algorithme de recuit simulé pour résoudre le TSP.
import math
import random
from problem import Problem  # Importer la classe de base Problem
from simulated_annealing import simulated_annealing  # Importer la classe simulated_annealing
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class TSP(Problem):
    def __init__(self, cities, dists):
        # Initialisation des villes et des distances
        self.cities = cities
        self.dists = dists
        self.sa = None

    def initial(self):
        # Générer un état initial aléatoire
        return random.sample(self.cities, len(self.cities))

    def cost(self, state):
        # Calculer le coût d'un état donné (chemin parcouru)
        # Le coût est la somme des distances entre les villes
        # Le chemin est circulaire, donc la distance entre la dernière et la première ville est incluse
        c = 0
        for i in range(len(self.cities)):
            c += self.dists[self.cities.index(state[i])][self.cities.index(state[(i + 1) % len(self.cities)])]
        return c

    def neighbor(self, state):
        # Générer un voisin en échangeant deux villes au hasard
        # Cela correspond à un mouvement 2-opt dans le TSP
        [a, b] = random.sample(range(len(self.cities)), 2)
        state[a], state[b] = state[b], state[a]
        return state
    
    def solve(self):
        # Résoudre le problème en utilisant le recuit simulé
        self.sa = simulated_annealing(self)
        return self.sa.solve()
    
    def update(self, frame, ax):
        # Mettre à jour l'animation pour chaque itération
        ax.clear()
        state = self.sa.states[frame]
        x = [self.cities.index(city) for city in state]
        y = [self.dists[self.cities.index(state[i])][self.cities.index(state[(i + 1) % len(state)])] for i in range(len(state))]
        ax.plot(x, y, 'bo-')
        ax.set_title(f'Iteration {frame}, Cost: {self.sa.progress[frame]}')
        ax.set_xlabel('City Index')
        ax.set_ylabel('Distance')
        plt.xticks(range(len(self.cities)), self.cities, rotation=90)
      
    def animate(self):
        # Animer le processus de recuit simulé
        fig, ax = plt.subplots()
        ani = animation.FuncAnimation(fig, self.update, frames=len(self.sa.states), fargs=(ax,), repeat=False, interval=10)
        plt.show()
        
    def show_final_graph(self):
        # Afficher le graphique final du meilleur chemin trouvé
        best = self.sa.states[-1]
        x = [self.cities.index(city) for city in best]
        y = [self.dists[self.cities.index(best[i])][self.cities.index(best[(i + 1) % len(best)])] for i in range(len(best))]
        plt.plot(x, y, 'bo-')
        plt.title(f'Final Solution, Cost: {self.sa.progress[-1]}')
        plt.xlabel('City Index')
        plt.ylabel('Distance')
        plt.xticks(range(len(self.cities)), self.cities, rotation=90)
        plt.show()
