#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define MAX_ELEMENTS 10

typedef struct Stack {
    int top; // index of the first element in the stack.
    int elements[MAX_ELEMENTS];
} Stack;

void createEmptyStack(Stack *stack) {
    stack->top = -1;
}

bool isFull(Stack *stack) {
    return (bool)(stack->top == MAX_ELEMENTS - 1); // Top is index based
}

bool isEmpty(Stack *stack) {
    return (bool)(stack->top == -1);
}

void push(Stack *stack, int elementToPush) {
    if (isFull(stack)) {
        printf("\nCannot push element, stack is full!\n");
        return;
    }

    stack->top++;
    stack->elements[stack->top] = elementToPush;
}

void pop(Stack *stack) {
    if(isEmpty(stack)) {
        printf("\nCannot pop stack, it's already empty!\n");
        return;
    }

    stack->elements[stack->top] = 0;
    stack->top--;
}

void printStack(Stack *stack) {
    if ( isEmpty(stack) ) {
        printf("\nStack is empty!\n");
        return;
    }

    int sizeOfStack = stack->top + 1;
    printf("\nStack:\n");
    for (int i = 0; i < sizeOfStack; i++) {
        if ( i == 0 ) printf("{\n");

        printf("    [%d] = %c\n", i, stack->elements[i]);

        if ( i == (sizeOfStack - 1) ) printf("}\n");
    }
}

// Testing of Stack DS

// int main() {
//     Stack *stack = (Stack *)calloc(1, sizeof(Stack));

//     createEmptyStack(stack);
//     push(stack, 10);
//     push(stack, 25);
//     push(stack, 50);
//     push(stack, 125);
    
//     printf("\nis Stack full?\n    %s\n", isFull(stack) ? "Yes!" : "No!");
//     printStack(stack);

//     pop(stack);
//     printStack(stack);

//     push(stack, 25);
//     push(stack, 50);
//     push(stack, 125);
//     push(stack, 250);
//     push(stack, 500);
//     push(stack, 1000);
//     push(stack, 2000);
//     push(stack, 4000);
//     push(stack, 8000);
//     push(stack, 16000);


//     printf("\nis Stack full?\n    %s\n", isFull(stack) ? "Yes!" : "No!");
//     printStack(stack);
    
//     return 0;
// }