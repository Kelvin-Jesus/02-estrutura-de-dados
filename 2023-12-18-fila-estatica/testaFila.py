from Fila import Fila, Item

f = Fila(5)

f.enfileira(Item('A'))
f.enfileira(Item('B'))
f.enfileira(Item('C'))
f.enfileira(Item('D'))
f.enfileira(Item('E'))

f.exibe()

f.desenfileira()
f.desenfileira()

f.exibe()

print(f.primeiroElemento().valor)

f.enfileira(Item('F'))

f.exibe()

print('Tamanho da fila =', f.tamanho())

f.esvazia()
f.exibe()