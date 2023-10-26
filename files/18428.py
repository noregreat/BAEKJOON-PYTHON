def backTracking(count):
  global flag
  if count == 3:
    if bfs():
      flag = True
      return
  else:
    for i in range(n):
      for j in range(n):
        if graph[i][j] == "X":
          graph[i][j] = "O"
          backTracking(count + 1)
          graph[i][j] = "X"


def bfs():
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  for t in tPos:
    for k in range(4):
      nx, ny = t
      while 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == "O":
          break
        if graph[nx][ny] == "S":
          return False

        nx += dx[k]
        ny += dy[k]
  return True


flag = False
n = int(input())
tPos = []

graph = [["X"] * n for _ in range(n)]
for i in range(n):
  graph[i] = input().split()
  for j in range(n):
    if graph[i][j] == "T":
      tPos.append((i, j))

backTracking(0)

if flag:
  print("YES")
else:
  print("NO")

#참고 : https://fre2-dom.tistory.com/436
#알고리즘 종류 공부 필요
