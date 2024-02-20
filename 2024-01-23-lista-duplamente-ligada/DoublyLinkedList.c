#include<stdlib.h>
#include<stdio.h>

typedef struct Node {
    struct Node *prev;
    int data;
    struct Node *next;
} Node;

Node* createEmptyNode() {
    struct Node *node = calloc(1, sizeof(Node));
    node->prev = node->next = NULL;

    return node;
}

int main() {
    Node* head = createEmptyNode();

    printf("", head->next);

    return 0;
}