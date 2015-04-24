import time
import random

currentMilliTime = lambda: int(round(time.time() * 1000))

#Default test array and random test generation vars.
testElements = [6, 9, 4, 7, 4, 1]
testSize = 3
maxArraySize = 50
minElement = 1
maxElement= 130
maxSize = 10

def deviation(v, d):
    dev = 0

    #For all items minus the last d elements
    for i in range(0, len(v)-d+1):
        #If the element is less than the greatest deviation to date
        #The deviation cannot be larger so skip this round entirely.
        if dev >= v[i]:
            continue

        #slice the array to only the needed part.
        slc = v[i:i+d]

        #calculate the deviation.
        tempDev = max(slc) - min(slc)

        #If it's bigger than the current max replace it.
        if dev < tempDev:
            dev = tempDev

    return dev

#make a list of num random numbers between minElement and maxElement.
def makeList(num):
    lst = [0 for i in range(0, num)]
    
    for i in range(0, num):
        lst[i] = random.randint(minElement, maxElement)

    return lst

numElements = random.randint(0, maxArraySize)

#make the list and pick the dev size.
lst = makeList(numElements)
size = random.randint(0, maxSize)

#time the run.
start = currentMilliTime()
result = deviation(lst, size)
end = currentMilliTime()

#Print results.
print("Time:{}".format(end - start))
print(result)
