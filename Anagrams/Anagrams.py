import time
import random
import string

currentMilliTime = lambda: int(round(time.time() * 1000))

#Default tests and random test generation configs.
firstWords = ['cinema','host','aba','train']
secondWords = ['iceman','shot','bab','rain']
maxWords = 100
maxWordSize = 5
shuffleChance = .95
wrongSizeChance = .05
letterChangeChance = .5

def anagrams(firstList, secondList):
    results = []

    #If the lists are not equal default out.
    if len(firstList) != len(secondList):
        return None

    #For all items
    for i in range(0, len(firstList)):
        first = firstList[i]
        second = secondList[i]

        #If the lengths are not the same they cannot be anagrams.
        if len(first) != len(second):
            #print('0')
            results.append('0')
            continue

        #If they are equal they are obviously anagrams.
        if first == second:
            #print(1)
            results.append('1')
            continue

        #Set up array of falses
        secondTaken = [False for x in range(0, len(second))]

        hasPrinted = False

        #For every letter in the first one
        for j in first:
            #If the second does not contain the letter they are not anagrams
            if not j in second:
                results.append('0')
                #print('0')
                hasPrinted = True
                break

            found = False

            #Search for the letter and space that is not taken
            #A particular letter can only be used once
            for k in range(0, len(second)):
                if j == second[k] and secondTaken[k] == False:
                    secondTaken[k] = True
                    found = True
                    break

            #If we did not find an available letter return 'False'
            if not found:
                results.append('0')
                #print('0')
                hasPrinted = True
                break

        #If we have not returned a result yet we need to do one now.
        if not hasPrinted:
            for j in secondTaken:
                #If all letters are not taken it is not an anagram.
                if j == False:
                    results.append('0')
                    #print('0')
                    break
            else:
                #print('1')
                results.append('1')
                continue
            
    return results

#Makes an initial word list
def makeWordList(numWords):
    letters = string.ascii_letters
    words = []

    #For numWords make 'words'
    for i in range(0, numWords):
        s = ''
        wordSize = random.randint(2, maxWordSize+1)

        #Append wordSize letters
        for j in range(1, wordSize):
            s += random.choice(letters)

        words.append(s)

    return words

#Shuffle, change size, and change letters.
def makeAnagrams(wordList):
    second = []

    for i in range(0, len(wordList)):
        word = wordList[i]
        
        if random.random() < shuffleChance:
            word = shuffle(word)

        if random.random() < wrongSizeChance:
            word = wrongSize(word)

        if random.random() < letterChangeChance:
            word = letterChange(word)

        second.append(word)

    return second

#Simple shuffle
def shuffle(word):
    return ''.join(random.sample(word, len(word)))

#Deletes numRemoved letters. Really one letter would be sufficient.
def wrongSize(word):

    if len(word) < 2:
         return word
        
    numRemoved = 1
    
    #If the length of the word is > 1 decide how many letters to delete.
    if len(word) > 1:
        numRemoved = random.randint(1, int(len(word) - (len(word) / 2)))
        
    w = word
    #Cast the word to a list.
    l = list(w)

    #Remove numRemoved letters from random spots.
    for i in range(0, numRemoved):
        del l[random.randint(0, len(l)-1)]

    #Cast the list to a word.
    w = ''.join(l)
    
    return w

#Changes a letter in a random spot to another letter.
def letterChange(word):
    
    numChanged = 1

    #If the length of the word is < 2 this will crash.
    if len(word) < 2:
        return word

    #Decide how many letters to change.
    if len(word) > 1:
        numChanged = random.randint(1, len(word))

    #Get a list of upper and lower case letters.
    letters = string.ascii_letters
    w = word

    
    for i in range(0, numChanged):
        changed = 0

        #Decide which index to change.
        if len(word) > 1:
            changed = random.randint(0, len(word)-1)

        #Cast the word to a list.
        l = ['' for i in range(0, len(word)-1)]
        l = list(word)
        #Change the letter
        l[changed] = random.choice(letters)
        #Cast the list to a word.
        word = ''.join(l)

    return word

numWords = random.randint(0, maxWords)

#Make a list and anagrams
first = makeWordList(numWords)
second = makeAnagrams(first)

results = []

#Time the algorithm.
startMillis = currentMilliTime()
results = anagrams(first, second)
endMillis = currentMilliTime()

t = endMillis - startMillis

#Print processing time and results.
print('Time:{}'.format(t))
for i in range(0, len(results)-1):
    print('{}, {}, {}'.format(results[i], first[i], second[i]))
