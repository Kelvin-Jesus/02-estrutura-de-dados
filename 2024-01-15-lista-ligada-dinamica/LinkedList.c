#include<stdio.h>
#include<stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;

} Node;

Node* createEmptyNode() {
    struct Node *node = calloc(1, sizeof(Node));
    node->next = NULL;
    
    return node;
}

int main() {
    Node* head;
    head = createEmptyNode();

    Node* red;
    red = createEmptyNode();
    red->data = 0xFF0000;

    head->next = red;

    Node* blue;
    blue = createEmptyNode();
    blue->data = 0x00FF00;

    red->next = blue;

    Node* green;
    green = createEmptyNode();
    green->data = 0x0000FF;

    blue->next = green;

    Node* current = head->next;
    while (current != NULL) {
        printf("Hex: %06X\n", current->data);
        current = current->next;
    }

    return 0;
}