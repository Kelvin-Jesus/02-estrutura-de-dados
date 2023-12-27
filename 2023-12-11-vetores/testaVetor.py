from vetor import Vetor

v = Vetor(5)

v[1] = 11

print(len(v))

print(v)

ind = 0
for i in v:
    print(ind, i)
    ind += 1

# a instrução abaixo gera um erro de execução,
# pois v não admite a operação append
# v.append(12)

print(len(v.itens))