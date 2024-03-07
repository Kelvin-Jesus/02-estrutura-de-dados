from arvore import *

def main():
    a = AB()
    a.insereRaiz(Item(1))
    a.insereNaEsq(Item(2), a.raiz)
    a.insereNaDir(Item(3), a.raiz)
    a.insereNaEsq(Item(4), a.raiz.filhoEsq)
    a.insereNaDir(Item(5), a.raiz.filhoEsq)
    a.exibe()

    b = AB()
    b.insereRaiz(Item(1))
    b.insereNaEsquerda(Item(2), Item(1))
    b.insereNaDireita(Item(3), Item(1))
    b.insereNaEsquerda(Item(4), Item(2))
    b.insereNaDireita(Item(5), Item(2))
    b.insereNaEsquerda(Item(6), Item(4))
    b.insereNaDireita(Item(7), Item(4))
    b.exibe()

    no = b.busca(Item(5))
    if no != None:
        print(no.elemento)
    else: print(no)
       
    print('Altura da árvore a:', a.altura())
    print('Altura da árvore b:', b.altura())

    print("Percurso em pré-ordem da árvore a:")
    a.percorreArvore(0)
    print("Percurso em in-ordem da árvore a:")
    a.percorreArvore(1)
    print("Percurso em pós-ordem da árvore a:")
    a.percorreArvore(2)

main()