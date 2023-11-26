// # Projete uma função que calcule a média aritmética de três números reais. 
// # A seguir, faça uma função rincipal (main) que peça para o usuário digitar 
// # três notas e imprima a média dessas notas.
#include <stdio.h>

float media_aritmetica(float n1, float n2, float n3) {
    return (n1 + n2 + n3) / 3;
}

int main() {
    printf("%.1f\n", media_aritmetica(5, 5, 8)); // 6.0
    printf("%.1f\n", media_aritmetica(3, 5, 6)); // 4.7
    printf("%.1f\n", media_aritmetica(10, 5, 8.5)); // 7.8
    return 0;
}