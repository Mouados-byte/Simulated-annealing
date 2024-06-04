from TSP import TSP

# Villes marocaines
cities = ['Casablanca', 'Rabat', 'Marrakech', 'Fes', 'Tangier', 'Agadir', 'Oujda', 'Meknes', 'Tetouan', 'Kenitra']
# Distances entre les villes marocaines
# Les distances sont en kilomètres et sont calculées à l'aide de Google Maps
dists = [
    [0, 87, 244, 294, 338, 464, 625, 236, 378, 120],
    [87, 0, 323, 206, 250, 546, 512, 138, 263, 40],
    [244, 323, 0, 484, 578, 256, 789, 450, 581, 356],
    [294, 206, 484, 0, 399, 668, 328, 64, 307, 177],
    [338, 250, 578, 399, 0, 837, 554, 358, 61, 211],
    [464, 546, 256, 668, 837, 0, 944, 676, 867, 586],
    [625, 512, 789, 328, 554, 944, 0, 392, 558, 474],
    [236, 138, 450, 64, 358, 676, 392, 0, 298, 117],
    [378, 263, 581, 307, 61, 867, 558, 298, 0, 231],
    [120, 40, 356, 177, 211, 586, 474, 117, 231, 0]
]

# Créer une instance du problème TSP avec les villes et les distances
problem = TSP(cities, dists)
# Résoudre le problème en utilisant le recuit simulé
best, best_cost = problem.solve()
# Animer le processus de résolution
problem.animate()
# Afficher le meilleur chemin trouvé et son coût
print(best, best_cost)
