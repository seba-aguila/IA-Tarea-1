from collections import deque
import numpy as np

def reconstruct_path(cameFrom, current):
  path = deque()
  path.appendleft(current)
  while current in cameFrom:
    current = cameFrom[current]
    path.appendleft(current)
  return path

def print_answer(path, costs, expanded, start):
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

def a_star(graph, h, costs, start, goal):
  open = {start: h[start]}
  cameFrom = {}
  g = {}
  for node in graph:
    g[node] = np.inf
  g[start] = 0
  expanded = {}
  for node in graph:
    expanded[node] = 0

  while len(open) > 0:
    nodes = list(open.keys())
    current = nodes[0]
    for i in range(1, len(open)):
      if open[nodes[i]] < open[current]:
        current = nodes[i]
    
    if current == goal:
      path = reconstruct_path(cameFrom, current)
      print_answer(path, costs, expanded, start)
      return

    open.pop(current)

    if len(graph[current]) > 0:
      expanded[current] += 1
    for neighbour in graph[current]:
      tentative_g = g[current] + costs[current, neighbour]
      if tentative_g < g[neighbour]:
        cameFrom[neighbour] = current
        g[neighbour] = tentative_g
        open[neighbour] = tentative_g + h[neighbour]

  print('Nodo objetivo no encontrado')
  return
