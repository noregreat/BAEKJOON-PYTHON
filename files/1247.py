for i in range(3):
    a = int(input())
    n = [int(input()) for _ in range(a)]
    s = sum(n)
    if s>0:
        print('+')
    elif s<0:
        print('-')
    else:
        print(0)
