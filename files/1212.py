inputNum = list(input())
inputNum = list(map(int, inputNum))

firstanswer = ["0", "1", "10", "11", "100", "101", "110", "111"]
answer = ["000", "001", "010", "011", "100", "101", "110", "111"]

for i in range(len(inputNum)):
  if (i == 0):
    print(firstanswer[inputNum[i]], end="")
  else:
    print(answer[inputNum[i]], end="")