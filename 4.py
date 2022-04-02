from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)


def dfs(curr, path):
  path.append(curr)
  
  if curr not in invNeighborMap:
    global paths
    
    paths.append(path)
    return
  
  for neighbor in invNeighborMap[curr]:
    dfs(neighbor, path.copy())

def handle(root):
  res = 0
  global paths, triggered
  paths = []
  
  if root not in invNeighborMap:
    return funFactors[root-1]
  
  for pointing in invNeighborMap[root]:
    dfs(pointing, [root])

  maximums = []
  
  for path in paths:
    funFactorPath = [funFactors[p-1] for p in path]
    funFactorPath.sort(reverse=True)
    maximums.append((funFactorPath, path))
    
  maximums.sort(key=lambda x: x[0])
  
  for mx, path in maximums:
    notTriggeredPath = []
    for node in path:
      if node not in triggered:
        notTriggeredPath.append(node)
        triggered.add(node)
    
    pathMax = max([funFactors[p-1] for p in notTriggeredPath])
    res += pathMax
  
  return res
  
  
def solve():
  global neighborMap, invNeighborMap, roots, triggered, funFactors
  neighborMap = {}
  invNeighborMap = defaultdict(list)
  triggered = set()
  roots = []
  
  N = int(input())
  funFactors = [int(x) for x in input().split()]
  neighs = [int(x) for x in input().split()]  
  
  
  for i in range(len(neighs)):
    neighborMap[i+1] = neighs[i]
    invNeighborMap[neighs[i]].append(i+1)
    if (neighs[i] == 0):
      roots.append(i+1)

  finalRes = 0
  for root in roots: 
    finalRes += handle(root)
  
  return finalRes
    
  
  
def main():
  N = int(input())

  results = []
  
  for _ in range(N):
    results.append(solve())
    
  for i in range(len(results)):
    print(f'Case #{i+1}: {results[i]}')
    
    
main()