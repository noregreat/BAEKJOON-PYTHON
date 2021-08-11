def gethansu(a):
  if a<100:
    return 1
  else :
    b=list(map(int,str(a)))
    if b[1] - b[0] == b[2] - b[1]:
      return 1
  return 0

hansu = 0
inp = int(input())
for i in range(1,inp+1):
    hansu+=gethansu(i)
print(hansu)