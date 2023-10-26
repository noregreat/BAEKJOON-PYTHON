n, w, L = map(int, input().split())
a = list(map(int, input().split()))
f = [w] * n
T = 0

while sum(f) > 0:
  T += 1
  tempL = L
  tempW = w
  for i in range(n):
    if tempL < a[i]:
      break
    if tempW <= 0:
      break
    if f[i] > 0:
      tempL -= a[i]
      if f[i] == w:
        tempW = 0
      else:
        tempW -= 1
      f[i] -= 1

print(T + 1)