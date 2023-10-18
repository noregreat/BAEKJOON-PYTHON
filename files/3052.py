i = [int(input()) for _ in range(10)]
j = []
for _ in range(10):
  a = i[_]%42
  if a not in j:
    j.append(a)
print(len(j))