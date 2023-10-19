numlist = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E',
    'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

num, format = input().split()
format = int(format)
num = list(num)

sum = 0
for i in range(len(num)):
  sum += numlist.index(num[i]) * (format**(len(num) - i - 1))

print(sum)