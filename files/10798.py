ary=[[0]*15 for _ in range(5)]

for i in range(5):
  ary[i]=list(input())

ary2=[[""]*5 for _ in range(15)]

for i in range(5):
  for j in range(len(ary[i])):
    ary2[j][i]=ary[i][j]

for i in range(15):
  print(*ary2[i],sep="",end="")