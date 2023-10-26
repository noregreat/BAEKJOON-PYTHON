N = int(input())
P = list(map(int, input().split()))
T = 0
PT = [0] * N

while sum(P) > 0:
  for i in range(N):
    if (P[i] > 0):
      T += 1
      P[i] -= 1
      PT[i] = T
    

print(*PT, sep=" ")