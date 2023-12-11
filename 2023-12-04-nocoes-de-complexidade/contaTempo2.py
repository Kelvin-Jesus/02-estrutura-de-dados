"""
Arquivo: contaTempo2.py 
Autor: Ken A. Lambert
Imprime os tempos de execução para tamanhos de problemas que dobram,
usando um laço aninhado. 
"""

import time

problemSize = 1000
print("%12s%16s" % ("Problem Size", "Seconds")) 
for count in range(5): 
    start = time.time() 
    # O início do algoritmo 
    work = 1 
    for j in range(problemSize): 
        for k in range(problemSize): 
            work += 1 
            work -= 1
    # O fim do algoritmo
    elapsed = time.time() - start 
    print("%12d%16.3f" % (problemSize, elapsed)) 
    problemSize *= 2
    