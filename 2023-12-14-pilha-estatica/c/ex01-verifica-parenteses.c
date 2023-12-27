#include<stdio.h>
#include<stdbool.h>
#include<string.h>
#include<stdlib.h>

#include "Stack.h"

bool isExpressionBalanced(char *expression) {
    Stack *stack = (Stack *)calloc(1, sizeof(Stack));

    createEmptyStack(stack);

    int expressionLength = strlen(expression);

    for (int i = 0; i < expressionLength; i++) {
        char caracter = expression[i];

        if (caracter == '(') {
            if (isFull(stack)) {
                printf("Cannot push, stack is full\n");
                return NULL;
            }

            push(stack, expression[i]);
        }
        else if (caracter == ')') {
            if (isEmpty(stack)) {
                return false;
            }

            pop(stack);
        }

    }

    return isEmpty(stack);
}

int main() {
    bool isBalanced;
    char* expression = "empilha(Item(c)))";
    // "empilha(Item(c))"; true
    // "print(round(media_aritmetica(n1, n2, n3),1))" true
    // "(2 * (a + b)" false
    // "empilha(Item(c)))" false
    
    isBalanced = isExpressionBalanced(expression);
    
    if (isBalanced) {
        printf("Is Balanced");
        return 0;
    }

    printf("Is not Balanced");
    return 0;
}
