sup = list(map(int, input().split()))
dem = list(map(int, input().split()))
result = [a - b for a, b in zip(sup, dem)]
print(sum(result))
