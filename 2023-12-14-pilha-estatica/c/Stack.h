#ifndef STACK_H
#define STACK_H

#include<stdbool.h>

#define MAX_ELEMENTS 10

typedef struct Stack {
    int top; // index of the first element in the stack.
    int elements[MAX_ELEMENTS];
} Stack;

void createEmptyStack(Stack *stack);
bool isFull(Stack *stack);
bool isEmpty(Stack *stack);
void push(Stack *stack, int elementToPush);
void pop(Stack *stack);
void printStack(Stack *stack);

#endif // STACK_H