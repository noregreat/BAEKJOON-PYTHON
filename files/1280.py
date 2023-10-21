N = int(input())
X = [0]*N
price = [0]*N
sum = 1

for i in range(N):
  X[i] = int(input())
  if(i>0):
    
    sum*=price[i]

print(price)
sum = int(sum%(1e9+7))
print(sum)