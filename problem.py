class Problem:
  def initial(self):
    raise NotImplementedError

  def cost(self, state):
    raise NotImplementedError

  def neighbor(self, state):
    raise NotImplementedError
  
  def solve(self):
    raise NotImplementedError