import time
import random

currentMilliTime = lambda: int(round(time.time() * 1000))

#Test and test generation vars
testList = [50,170,205,23,196,168,16,27,148,4]
maxNums = 5000
maxNumSize = 230

def hill(v):

    #Apply a decreasing weight to each number.
    for i in range(0, len(v)):
        v[i] = v[i] - i

    #the answer is max - min of the new array over 2 rounded.
    dev = (max(v) - min(v)) / 2

    return int(round(dev))

lst = []
lstSize = random.randint(0, maxNums)

#Make a random array between 0 and lstSize
for i in range(0, lstSize):
    #make random numbers for the array between 1 and maxNumSize
    lst.append(random.randint(1, maxNumSize))

#Time the run.
start = currentMilliTime()
result = hill(lst)
end = currentMilliTime()

#Print results
print('Time:{}'.format(end - start))
print('Result:{}'.format(result))
