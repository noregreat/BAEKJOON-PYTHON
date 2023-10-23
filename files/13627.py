R,N = map(int,input().split())
plist = list(range(1,R+1))

P = list(map(int,input().split()))

for i in P:
  plist.remove(i)

if(len(plist)==0):
  print("*")
else:
  print(*plist,sep=" ")