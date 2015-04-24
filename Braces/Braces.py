import time

currentMilliTime = lambda: int(round(time.time() * 1000))

braces = [ ")(){}", "[]({})", "([])", "{()[]}", "([)]" ]

def braceCheck(expressions):
    results = []

    for i in expressions:
        results.append(check(i))
    return results

def check(expression):
    opening = ['(','{','[']
    closing = [')','}',']']

    stack = []

    for i in expression:
        #If it's an opening brace push
        if i in opening:
            stack.append(i)
        #Else it's a closing brace
        else:
            #If the stack is empty return 'False'
            if len(stack) < 1:
                return '0'

            #Else pop the top item.
            e = stack.pop()

            #If items are not paired return 'False'
            if closing.index(i) != opening.index(e):
                return '0'
            else:
                return '1'

results = []

#Time how long it takes to run.
startMillis = currentMilliTime()
results = braceCheck(braces)
endMillis = currentMilliTime()

time = endMillis - startMillis

#Print time and results.
print('Time:{}'.format(time))
for i in results:
    print(i)

#TODO: Design random tests.
