J,R = list(map(int,input().split()))
ary = list(map(int,input().split()))
playersScore = [0]*J

for i in range(len(ary)):
  playersScore[i%J] += ary[i]

playersScore.reverse()
print(J-(playersScore.index(max(playersScore))))