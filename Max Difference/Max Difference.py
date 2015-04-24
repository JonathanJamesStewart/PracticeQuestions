import time
import random

currentMilliTime = lambda: int(round(time.time() * 1000))

#Default tests and random test generation vars
testArr = [3, -5, 1, -2, 8, -2, 3, -2, 1]
minArrSize = 2
maxArrSize = 1000000
minNumSize = -1000
maxNumSize = 1000

def maxDifference(v):
    maxEndingHere = maxSoFar = v[0]

    for x in v[1:]:
        maxEndingHere = max(x, maxEndingHere + x)
        maxSoFar = max(maxSoFar, maxEndingHere)

    minEndingHere = minSoFar = v[0]

    for x in v[1:]:
        minEndingHere = min(x, minEndingHere + x)
        minSoFar = min(minSoFar, minEndingHere)

    return maxSoFar - minSoFar

arrSize = random.randint(2, maxArrSize)
arr = []

for i in range(0, arrSize):
    arr.append(random.randint(minNumSize, maxNumSize))

start = currentMilliTime()
result = maxDifference(arr)
end = currentMilliTime()

print('Time:{}'.format(end - start))
print('Result:{}'.format(result))
