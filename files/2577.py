n = [int(input()) for _ in range(3)]
s = str(n[0] * n[1] * n[2])
for i in range(10):
  print(s.count(str(i)))