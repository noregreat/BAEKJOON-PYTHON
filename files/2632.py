def findCase(piz, len):
  case = {}
  for i in range(len):
    tmp = piz[i:] + piz[:i]
    scase = 0
    for j in tmp:
      scase += j
      if scase in case:
        case[scase] += 1
      else:
        case[scase] = 1
  case[sum(piz)] = 1
  return case


n = int(input())
a_cnt, b_cnt = map(int, input().split())
a = [int(input()) for _ in range(a_cnt)]
b = [int(input()) for _ in range(b_cnt)]
aCase = findCase(a, a_cnt)
bCase = findCase(b, b_cnt)

result = aCase.get(n, 0) + bCase.get(n, 0)

for i in aCase:
  if n - i in bCase:
    result += aCase[i] * bCase[n - i]

print(result)

#25번쨰 줄에서 정답 구할 때 이중 for문 사용했다가 시간초과 떠서 수정함..
