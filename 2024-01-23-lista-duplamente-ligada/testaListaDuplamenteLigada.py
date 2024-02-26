from ListaDuplamenteLigada import *

# Testes para `estaVazia`

lista = ListaDuplamenteLigada()
print(f"Lista vazia: {lista.estaVazia()}")

lista.insereNoInicio(Item(10))
print(f"Lista com um elemento: {lista.estaVazia()}")

lista.insereNoInicio(Item(20))
print(f"Lista com vários elementos: {lista.estaVazia()}")

# Testes para `insereNoInicio`

lista = ListaDuplamenteLigada()
lista.insereNoInicio(Item(10))
lista.exibe()

lista = ListaDuplamenteLigada()
lista.insereNoInicio(Item(10))
lista.insereNoInicio(Item(20))
lista.exibe()

lista = ListaDuplamenteLigada()
for i in range(10):
    lista.insereNoInicio(Item(i))
lista.exibe()

# Testes para `insereNoFim`

lista = ListaDuplamenteLigada()
lista.insereNoFim(Item(10))