'''
    Função principal: 
    - lê números inteiros até o usuário digitar um valor negativo; 
    - armazena os valores lidos (exceto o valor negativo) em uma lista
    - em seguida, exibe todos os valores lidos, bem como a média aritmética desses valores.
'''

def mediaAritmeticaDeUmaLista(listaDeInteiros: list) -> int:
    soma = 0
    for inteiro in listaDeInteiros:
        soma += inteiro

    return soma // len(listaDeInteiros)

def main() -> None:
    print("Digite uns números inteiros aí. Qando terminar, digite um número negativo")
    listaDeInteiros: list = []

    inteiro: int = 0
    while(True):
        inteiro = int(input())
        if inteiro <= 0:
            break

        listaDeInteiros.append(inteiro)

    print(f"\nOs números digitados foram: {listaDeInteiros}")
    print(f"\nA média artimética dos valores digitados é: {mediaAritmeticaDeUmaLista(listaDeInteiros)}")

if __name__ == "__main__":
    main()