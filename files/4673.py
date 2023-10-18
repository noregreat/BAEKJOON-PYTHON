l = list(range(1,10001))
n = []
for i in l:
  for j in str(i):
    i+=int(j)
  if i<=10000:
    n.append(i)
for i in set(n):
  l.remove(i)
for i in l:
  print(i)