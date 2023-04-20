import random

def dfs(graph, costs, start, goal):
  visited = []
  path = []
  expanded = {}
  for node in graph:
    expanded[node] = 0

  def visitNode(node):
    visited.append(node)
    path.append(node)
    # If we reached the goal
    if node == goal:
      return
    if len(graph[node]) == 0:
      path.pop()
      return
    neighbours = graph[node].copy()
    if len(neighbours) > 0:
      expanded[node] += 1
    while len(neighbours) > 0:
      if path[-1] == goal:
        return
      next = random.choice(neighbours)
      neighbours.remove(next)
      visitNode(next)

  visitNode(start)
  
  if path[-1] != goal:
    print('Nodo objetivo no encontrado')
    return
  
  totalCost = 0
  for i in range(len(path) - 1):
    totalCost += costs[path[i], path[i + 1]]
    print(path[i] + ' -> ', end='')
  print(path[-1])
  print('Costo:', totalCost)
  
  print(start + ':', expanded[start])
  for node in expanded:
    if node != start:
      print(node + ':', expanded[node])