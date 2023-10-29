from itertools import permutations

n, k = map(int, input().split())
a = list(map(int, input().split()))
cases = permutations(a, n)

result = 0

for case in cases:
  wei = 500
  for i in case:
    wei += i - k
    if wei < 500:
      break
  if wei >= 500:
    result += 1

print(result)

#순열 구하는 것 때문에 실버3인 것 같은데.. 파이썬 라이브러리가 있어서 너무 쉽게 풀렸다.
#나중에 라이브러리 없이 다시 풀어봐야겠다.
