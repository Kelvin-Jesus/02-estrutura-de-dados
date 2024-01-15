from listaEstatica import ListaEstatica, Item

l = ListaEstatica(5)

l.insere(Item('a'))
l.insere(Item('b'))
l.insere(Item('c'))
l.insere(Item('d'))

try:
    l.insereNaPosicao(Item('A'), 0)
except ValueError:
    print('Erro na inserção')

try:
    l.removeNaPosicao(5)
except ValueError:
    print('Erro na remoção: pos inválida')

try:
    l.removeElemento(Item('e'))
except ValueError:
    print('Erro na remoção: elemento inexistente')


l.exibe()

print(l.tamanho())

print(l.ultimo())

print(l.estaCheia())

l.esvazia()
l.exibe()

try:
    l.insere(Item('e'))
except ValueError:
    print('Erro na inserção')

l.exibe()
print(l.tamanho())

print(l.primeiro())
print(l.ultimo())

try:
    print(l.buscar(Item('e')))
except ValueError:
    print('Elemento não encontrado')