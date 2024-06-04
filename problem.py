class Problem:
    # Méthode pour générer l'état initial
    def initial(self):
        raise NotImplementedError

    # Méthode pour calculer le coût d'un état donné
    def cost(self, state):
        raise NotImplementedError

    # Méthode pour générer un voisin d'un état donné
    def neighbor(self, state):
        raise NotImplementedError
    
    # Méthode pour résoudre le problème
    def solve(self):
        raise NotImplementedError
    
    # Méthode pour animer le processus de résolution
    def animate(self, frame):
        raise NotImplementedError
