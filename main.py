from collections import defaultdict
from dfs import dfs
from ucs import ucs
from greedy import greedy
from a_star import a_star

with open('input.txt', 'r') as file:
  # Reading start and goal points
  line = file.readline()
  [title, start] = line.split()
  line = file.readline()
  [title, goal] = line.split()
  
  # Reading heuristic values
  h = {} # Dictionary for heuristics
  while True:
    line = file.readline()
    if line.find(',') != -1:
      break
    [node, heuristic] = line.split()
    h[node] = int(heuristic)

  # Building graph
  graph = defaultdict(list)
  costs = {}
  [x, y, c] = line.split(', ')
  graph[x].append(y)
  graph[y] = []
  costs[x, y] = int(c)
  while True:
    line = file.readline()
    if not line:
      break
    [x, y, c] = line.split(', ')
    graph[x].append(y)
    if y not in graph:
      graph[y] = []
    costs[x, y] = int(c)

print('DSF:')
dfs(graph, costs, start, goal)
print('\nUCS:')
ucs(graph, costs, start, goal)
print('\nGreddy:')
greedy(graph, costs, h, start, goal)
print('\nA*:')
a_star(graph, h, costs, start, goal)