piboList = [[1, 0], [0, 1]]

for i in range(2, 41):
  piboList.append([
      piboList[i - 1][0] + piboList[i - 2][0],
      piboList[i - 1][1] + piboList[i - 2][1]
  ])

testCount = int(input())
testNum = [0] * testCount
for i in range(testCount):
  testNum[i] = int(input())

for i in range(testCount):
  print(*piboList[testNum[i]], sep=" ")