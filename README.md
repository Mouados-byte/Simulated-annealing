# Simulated Annealing (Recuit simulé):

## Description:
Le recuit simulé est une méthode d'optimisation stochastique qui permet de trouver le minimum global d'une fonction. Cette méthode est inspirée du processus de refroidissement des métaux. En effet, lorsqu'un métal est chauffé à haute température, les atomes se déplacent de manière aléatoire. En refroidissant, les atomes se figent dans une configuration stable. L'idée du recuit simulé est de simuler ce processus en définissant une température initiale élevée qui diminue progressivement. A chaque itération, un voisin du point courant est généré et la fonction objectif est évaluée. Si la solution est meilleure, elle est acceptée. Sinon, elle est acceptée avec une probabilité qui dépend de la différence entre la solution courante et la solution voisine et de la température courante. Cette probabilité diminue au fur et à mesure que la température diminue. Ainsi, le recuit simulé permet d'éviter de rester bloqué dans un minimum local en acceptant des solutions moins bonnes avec une certaine probabilité.

https://github.com/Mouados-byte/Simulated-annealing/assets/74561965/40fee6f0-43cc-43e6-8a65-581f4bd554f4

## References:
- [Wikipedia - Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing)
