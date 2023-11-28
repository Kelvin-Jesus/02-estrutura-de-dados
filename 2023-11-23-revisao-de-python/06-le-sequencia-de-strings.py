'''
    Função principal:
    - lê strings do teclado até que o usuário digite uma string vazia; 
    - armazena todas as strings lidas em uma lista; 
    - em seguida, exibe todas as strings lidas na tela.
'''

def main() -> None:
    print("Digite umas frases aí. Qando terminar, tecle ENTER")
    listaDeStrings: list = []

    frase: str = ''
    while(True):
        frase = input()
        if len(frase) <= 0:
            break

        listaDeStrings.append(frase)

    print("Você digitou:")
    for palavra in listaDeStrings:
        print(palavra)

    print("\nA frase ficaria: " + ' '.join(listaDeStrings))

if __name__ == "__main__":
    main()