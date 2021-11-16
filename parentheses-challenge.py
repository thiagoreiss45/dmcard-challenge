import random
import time
start_time = time.time()
f = open("myfile100.txt", "r")

def isExpressionValid(exp):
    var = 0
    for c in exp:
        if var < 0:
            return 'incorrect'
        elif c == '(':
            var += 1
        elif c == ')':
            var -=1
    if var == 0:
        return 'correct'
    else:
        return 'incorrect'

output = open("output.txt", "w")
aux = 0
for l in f:
    if aux == 0:
        output.write(isExpressionValid(l))
        aux += 1
    else:
        output.write('\n' + isExpressionValid(l))
output.close()
f.close()
print("--- %s seconds ---" % (time.time() - start_time))