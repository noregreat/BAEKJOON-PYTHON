H, W, X, Y = list(map(int,input().split()))

aryA = [[0]*W for _ in range(H)]
aryB = [[0]*(W+Y) for _ in range(H+X)]

for i in range(H+X):
  aryB[i] = list(map(int,input().split()))

for i in range(H):
  for j in range(W):
    if i<X or j<Y:
      aryA[i][j] = aryB[i][j]
    elif aryB[i][j] == 0:
      aryA[i][j] = 0
    else:
      aryA[i][j]= aryB[i][j] - aryA[i-X][j-Y]

for temp in aryA:
  print(*temp,sep=" ")