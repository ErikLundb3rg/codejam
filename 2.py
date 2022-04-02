from collections import defaultdict

INF = 10e15


def findMinimumForColor(color, printers): 
  mn = INF
  for printer in printers:
    mn = min(mn, printer[color])
  return mn

def solve():
  printers = []
  
  for _ in range(3):
    printers.append([int(x) for x in input().split(' ')])
  
  res = []
  amountLeft = int(1e6)
  
  for color in range(4):
    if amountLeft == 0:
      res.append(0)
      continue 
    
    taken = findMinimumForColor(color, printers)
    
    if amountLeft-taken < 0:
      taken = amountLeft
    
    amountLeft -= taken
    res.append(taken)

  if (amountLeft > 0):
    return 'IMPOSSIBLE'
  
  return " ".join([str(x) for x in res])
  
  
  
def main():
  N = int(input())

  results = []
  
  for _ in range(N):
    results.append(solve())
    
  for i in range(len(results)):
    print(f'Case #{i+1}: {results[i]}')
    
    
main()