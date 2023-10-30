n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a,b = map(int,input().split())
  graph[b].append(a)

def dfs(num):
  global visited
  visited[num] = True
  for i in graph[num]:
    if visited[i] == False:
      dfs(i)
      visited[i] = True
  
flag = -1
for i in range(n+1):
  visited = [False]*(n+1)
  dfs(i)
  if visited.count(True) == n:
    flag=i
    break
print(flag)