from pilha import Pilha, Item

p = Pilha(5)

p.empilha(Item('D'))
p.empilha(Item('C'))
p.empilha(Item('B'))
p.empilha(Item('F'))
p.empilha(Item('E'))

p.desempilha()

p.exibe()

print(p.elementoTopo())

p.empilha(Item('X'))
print(p.estaVazia())

p.estaVazia()
p.exibe()

print(len(p.elementos))