inputNumList = list(map(int, input().split(' ')))
answer = [1, 2, 3, 4, 5]

while (inputNumList != answer):
  for older in range(4):
    if (inputNumList[older] > inputNumList[older + 1]):
      temp = inputNumList[older]
      inputNumList[older] = inputNumList[older + 1]
      inputNumList[older + 1] = temp
      print(*inputNumList, sep=' ')