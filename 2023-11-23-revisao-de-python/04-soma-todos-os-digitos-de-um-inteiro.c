// # Projete uma função que calcule a soma dos dígitos de um número inteiro. 
// # A seguir, faça uma função principal que peça para o usuário digitar 
// # um número inteiro e informe a soma dos seus dígitos.
#include <stdio.h>

int soma_digitos(int n) {
    int soma = 0;
    while (n != 0) {
        soma += n % 10;  // pega somente o último digito de N
        n /= 10;  // Remove o último inteiro de N
    }

    return soma;
}

int main() {
    printf("%d\n", soma_digitos(5)); // 5
    printf("%d\n", soma_digitos(10)); // 1
    printf("%d\n", soma_digitos(123)); // 6
    printf("%d\n", soma_digitos(12345)); // 15
}