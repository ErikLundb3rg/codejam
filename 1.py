



def solve():
  R, C = map(int, input().split(' '))

  X = (R*2)+1
  Y = (C*2)+1
  res = []
  
  res.append(".." + "".join(['+' if i % 2 == 0 else '-' for i in range(Y-2)]))
  
  for i in range(R):
    if i == 0:
      res.append('..' +  "".join(['|' if j % 2 == 0 else '.' for j in range(Y-2)]))
    else:
      res.append("".join(['|' if j % 2 == 0 else '.' for j in range(Y)]))
    res.append("".join(['+' if j % 2 == 0 else '-' for j in range(Y)]))
  
  return '\n'.join(res)


def main():
  N = int(input())

  results = []
  
  for _ in range(N):
    results.append(solve())
    
  for i in range(len(results)):
    print(f'Case #{i+1}:')
    print(results[i])
    
    
main()