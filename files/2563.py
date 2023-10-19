background = [[0] * 100 for _ in range(100)]

count = int(input())

for i in range(count):
  x, y = list(map(int, input().split()))
  for xx in range(x, x + 10):
    for yy in range(y, y + 10):
      background[xx][yy] = 1

sum = 0
for i in range(100):
  sum += background[i].count(1)
print(sum)