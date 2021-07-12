a,b=input().split()
a=int(a)
b=int(b)

if b>=45:
    b-=45
else:
    a-=1
    b+=15
if a<0:
    a+=24
print(a,b)
