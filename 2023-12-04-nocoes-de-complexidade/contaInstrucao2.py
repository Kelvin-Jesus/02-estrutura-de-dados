"""
Arquivo: contaInstrucao2.py 
Autor: Ken A. Lambert
Imprime o número de iterações para tamanhos de problemas que dobram,
usando um laço aninhado. 
"""

import time

problemSize = 1000
print("%12s%15s" % ("Tam Problema", "Iterações")) 
for count in range(5): 
    number = 0
    # O início do algoritmo 
    work = 1 
    for j in range(problemSize): 
        for k in range(problemSize): 
            number += 1
            work += 1 
            work -= 1
    # O fim do algoritmo
    print("%12d%15d" % (problemSize, number)) 
    problemSize *= 2
    