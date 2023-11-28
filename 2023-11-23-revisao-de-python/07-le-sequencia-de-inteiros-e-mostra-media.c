// '''
//     Função principal: 
//     - lê números inteiros até o usuário digitar um valor negativo; 
//     - armazena os valores lidos (exceto o valor negativo) em uma lista
//     - em seguida, exibe todos os valores lidos, bem como a média aritmética desses valores.
// '''
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

int mediaAritmeticaDeUmaLista(int* listaDeInteiros, int tamanhoDaLista) {
    int soma = 0;

    for (int i = 0; i < tamanhoDaLista; i++)
        soma += listaDeInteiros[i];

    return soma / tamanhoDaLista;
}

int main() {
    printf("Digite uns números inteiros aí. Qando terminar, digite um número negativo\n");
    int* listaDeInteiros = NULL;

    int quantidadeDeInteiros = 0;
    int inteiroDigitado = 0;

    while(true) {
        scanf("%d", &inteiroDigitado);
        if (inteiroDigitado <= 0) break;

        listaDeInteiros = realloc(listaDeInteiros, (quantidadeDeInteiros + 1) * sizeof(int));
        listaDeInteiros[quantidadeDeInteiros] = inteiroDigitado;
        quantidadeDeInteiros++;
    }

    int media = mediaAritmeticaDeUmaLista(listaDeInteiros, quantidadeDeInteiros);
    printf("\nA média artimética dos valores digitados é: %d", media);
}