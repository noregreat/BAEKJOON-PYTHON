n = int(input())
for q in range(n):
  i = list(map(int,input().split()))
  i.remove(i[0])
  a=len(i)
  b=0
  c=sum(i)/a
  for w in range(a):
    if i[w]>c:
      b+=1
  print("{0:.3f}%".format(round(b/a*100,3)))