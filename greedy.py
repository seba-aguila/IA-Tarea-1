def greedy(graph, costs, h, start, goal):
  path = []
  expanded = {}
  for node in graph:
    expanded[node] = 0
  
  node = start
  while True:
    path.append(node)
    if node == goal:
      break
    if len(graph[node]) == 0:
      print('Nodo objetivo no encontrado')
      return
    expanded[node] += 1
    neighbours = graph[node]
    next = neighbours[0]
    for i in range(1, len(neighbours)):
      if h[neighbours[i]] < h[next]:
        next = neighbours[i]
    node = next
  
  totalCost = 0
  for i in range(len(path) - 1):
    totalCost += costs[path[i], path[i + 1]]
    print(path[i] + ' -> ', end='')
  print(path[-1])
  print('Costo:', totalCost)

  print(start + ':', expanded[start])
  for node in graph:
    if node != start and node != goal:
      print(node + ':', expanded[node])