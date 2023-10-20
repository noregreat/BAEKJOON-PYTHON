R, C, N = list(map(int, input().split()))
ary = [[0] * C for _ in range(R)]
for i in range(R):
  temp_ = list(map(str, input()))
  for j in range(C):
    if temp_[j] == 'O':
      ary[i][j] = 1
    else:
      ary[i][j] = 0

for i in range(N):
  for j in range(R):
    for k in range(C):
      if ary[j][k]>0 and ary[j][k] < 4:
        ary[j][k]+=1

      if i%2 == 1 :
        if ary[j][k] == 0:
          ary[j][k] = 1
      else:
        if ary[j][k] >= 4:
          ary[j][k] = 0
          for x,y in [0,1],[1,0],[0,-1],[-1,0]:
            if(j+x>=0 and j+x<R and k+y >= 0 and k+y < C):
              ary[j+x][k+y] = 0 if ary[j+x][k+y]<4 and x+y <= 0 else 4 if ary[j+x][k+y]>=3 else 0
      
for i in range(R):
  for j in range(C):
    if ary[i][j] > 0:
      print("O", end='')
    else:
      print(".", end='')
  print("")