ary =[[0]*9 for _ in range(9)]
max = 
maxRow = 0
maxCol = 0

for i in range(9):
  ary[i] = list(map(int,input().split()))
  for j in range(9):
    if(ary[i][j]>max):
      max=ary[i][j]
      maxRow=i+1
      maxCol=j+1

print(max)
print(maxRow, maxCol,sep=" ")