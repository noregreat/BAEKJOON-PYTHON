col, row = map(int,input().split())

ary1 = [[0]*row for _ in range(col)]
ary2 = [[0]*row for _ in range(col)]

for i in range(col):
  ary1[i] = list(map(int,input().split()))
for i in range(col):
  ary2[i] = list(map(int,input().split()))

for i in range(col):
  for j in range(row):
    ary1[i][j] += ary2[i][j]

for row_ in ary1:
  print(*row_,sep=" ")
  