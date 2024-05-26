from TSP import TSP


cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
dists = [
    [0, 29, 20, 21, 16, 31, 100],
    [29, 0, 15, 29, 28, 40, 72],
    [20, 15, 0, 15, 14, 25, 81],
    [21, 29, 15, 0, 4, 12, 92],
    [16, 28, 14, 4, 0, 16, 95],
    [31, 40, 25, 12, 16, 0, 97],
    [100, 72, 81, 92, 95, 97, 0]
]

problem = TSP(cities, dists)
best, best_cost = problem.solve()
print(best, best_cost)

