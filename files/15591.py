def usado(k, v):
  visited = [False]*(N+1)
  not_visited = [[v, 1000000000]]
  while not_visited:
    a, r = not_visited.pop()
    if not visited[a] and r>=k:
      not_visited.extend(G[a])
      visited[a] = True
  return visited.count(True)-1

N, Q = map(int,input().split())

G = {}

for i in range(N-1):
  p,q,r = map(int,input().split())
  if p in G:
    G[p].append([q,r])
  else:
    G[p] = [[q,r]]
  if q in G:
    G[q].append([p,r])
  else:
    G[q] = [[p,r]]

output = []
for i in range(Q):
  k,v = map(int,input().split())
  output.append(usado(k,v))
print(*output,sep="\n")