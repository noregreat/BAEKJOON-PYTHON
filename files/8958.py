n = int(input())
for q in range(n):
  i = str(input())
  a=0
  s=0
  for w in range(len(i)):
    if i[w]=="O":
      a+=1
      s+=a
    else:
      a=0
  print(int(s))