n = int(input())
hills = [int(input()) for _ in range(n)]
highs = [0] * n
amount = 0
while (max(hills) - min(hills) > 17):
  index_max = [i for i, ele in enumerate(hills) if ele == max(hills)]
  index_min = [i for i, ele in enumerate(hills) if ele == min(hills)]
  amount_Max = 0
  amount_Min = 0
  for i in index_max:
    amount_Max += (highs[i] + 1)**2 - (highs[i])**2
  for i in index_min:
    amount_Min += (highs[i] + 1)**2 - (highs[i])**2

  if amount_Max > amount_Min:
    for i in index_min:
      hills[i] += 1
      highs[i] += 1
  else:
    for i in index_max:
      hills[i] -= 1
      highs[i] += 1
for i in highs:
  amount += i**2
print(amount)
