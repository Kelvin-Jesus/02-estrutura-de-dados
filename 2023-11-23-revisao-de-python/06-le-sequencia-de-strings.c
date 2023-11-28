// '''
//     Função principal:
//     - lê strings do teclado até que o usuário digite uma string vazia; 
//     - armazena todas as strings lidas em uma lista; 
//     - em seguida, exibe todas as strings lidas na tela.
// '''
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int main() {
    printf("Digite umas frases ai. Qando terminar, tecle ENTER\n");
    char* listaDeStrings[255];

    int quantidadeStringsInseridas = 0;
    while(true) {
        char* frase = malloc(255);
        fgets(frase, sizeof(frase), stdin);

        if (frase[0] == '\n')
            break;

        listaDeStrings[quantidadeStringsInseridas] = frase;
        quantidadeStringsInseridas++;
    }

    printf("Você digitou:\n");
    for ( int i = 0; i < quantidadeStringsInseridas; i++ ) {
        printf("%s", listaDeStrings[i]);
    }
}