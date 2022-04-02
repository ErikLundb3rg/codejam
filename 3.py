


from collections import defaultdict

INF = 1e15


def solve():
  N = int(input()) 
  dices = [int(x) for x in input().split(' ')]
  dices.sort()
  
  
  count = 0
  
  for dice in dices:
    if dice > count:
      count += 1
      
  return count
  
  
def main():
  N = int(input())

  results = []
  
  for _ in range(N):
    results.append(solve())
    
  for i in range(len(results)):
    print(f'Case #{i+1}: {results[i]}')
    
    
main()