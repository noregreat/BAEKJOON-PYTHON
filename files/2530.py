inputTime = list(map(int,input().split()))
inputDelay = int(input())

inpMin = inputTime[0]*60 + inputTime[1]
inpSec = inpMin*60 + inputTime[2] + inputDelay

inputTime[2]= inpSec%60
tmp = int((inpSec - inputTime[2])/60)
inputTime[1] = tmp%60
inputTime[0] = int((tmp-inputTime[1])/60)
inputTime[0] = inputTime[0]%24

print(*inputTime,sep=" ")