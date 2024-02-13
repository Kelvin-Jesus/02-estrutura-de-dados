from listaLigada import *

l = ListaLigada()
l.insereNoInicio(Item('A'))
l.insereNoFim(Item('B'))
l.insereNaPosicao(Item('C'), 2)
l.insereNoFim(Item('D'))
l.exibe()

l.insereNaPosicao(Item('Z'), 0)
l.insereNaPosicao(Item('E'), 5)
l.insereNoFim(Item('F'))

l.exibe()
print(l.tamanho())

print(l.buscaNaPosicao(5))

print(l.busca(Item('A')))

l.removeElemento(Item('Z'))
l.removeElemento(Item('A'))
l.removeElemento(Item('B'))
l.removeElemento(Item('C'))
l.removeElemento(Item('D'))
l.removeElemento(Item('E'))
l.exibe()
print(l.tamanho())

l.insereNoFim(Item('A'))
l.insereNoFim(Item('B'))
l.insereNoFim(Item('C'))
l.insereNaPosicao(Item('D'), 2)
l.exibe()
print(l.tamanho())

l.removeNaPosicao(1)
l.exibe()
print(l.tamanho())

no = l.buscaNaPosicao(2)
if no != None:
    print(no.elemento.valor)
