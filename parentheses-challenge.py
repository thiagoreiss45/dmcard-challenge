import random
import time

start_time = time.time()

input_file = open("insira_aqui_o_arquivo", "r")
output_file = open("output.txt", "w")

def isExpressionValid(exp):
    var = 0
    for c in exp:
        if var < 0:
            return 'incorrect'
        elif c == '(':
            var += 1
        elif c == ')':
            var -= 1
    if var == 0:
        return 'correct'
    else:
        return 'incorrect'

# Percorrendo cada linha do arquivo de input e escrevendo o retorno no arquivo de output
is_first_line = True
for line in input_file:
    if is_first_line:
        output_file.write(isExpressionValid(line))
        is_first_line = False
    else:
        output_file.write('\n' + isExpressionValid(line))

output_file.close()
input_file.close()

# Printando o tempo de execução do programa
print("Execution time: %s seconds " % (time.time() - start_time))