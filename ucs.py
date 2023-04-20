from queue import PriorityQueue
from collections import deque
import numpy as np

def ucs(graph, weight, start, goal):
  cost = {}
  for node in graph:
    cost[node] = np.inf
  cost[goal] = np.inf
  cameFrom = {}
  frontier = PriorityQueue()
  cost[start] = 0
  frontier.put((cost[start], start))

  expanded = {}
  for node in graph:
    expanded[node] = 0
  
  while True:
    if frontier.empty():
      print('Nodo objetivo no encontrado')
      return
    current = frontier.get()[1]
    if current == goal:
      break
    if len(graph[current]) > 0:
      expanded[current] += 1
    for neighbour in graph[current]:
      if cost[neighbour] > cost[current] + weight[current, neighbour]:
        cost[neighbour] = cost[current] + weight[current, neighbour]
        frontier.put((cost[neighbour], neighbour))
        cameFrom[neighbour] = current

  path = deque()
  node = goal

  path.appendleft(node)
  while node in cameFrom:
    node = cameFrom[node]
    path.appendleft(node)

  totalCost = 0
  for i in range(len(path) - 1):
    totalCost += weight[path[i], path[i + 1]]
    print(path[i] + ' -> ', end='')
  print(path[-1])
  print('Costo:', totalCost)

  print(start + ':', expanded[start])
  for node in graph:
    if node != start:
      print(node + ':', expanded[node])