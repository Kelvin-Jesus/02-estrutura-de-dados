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

void insertAtBeginning(Node** head, int data) {
    Node* newNode = createEmptyNode();
    newNode->data = data;

    newNode->next = (*head);

    newNode->prev = NULL;
    if ( (*head) != NULL )
        (*head)->prev = newNode;

    (*head) = newNode;
}

void insertAfter(Node* prevNode, int data) {
    if (prevNode == NULL) {
        printf("Previous node cannot be NULL");
        return;
    }

    Node* newNode = createEmptyNode();
    newNode->data = data;

    newNode->next = prevNode->next;
    prevNode->next = newNode;
    newNode->prev = prevNode;

    if (newNode->next != NULL) 
        prevNode->next->prev = newNode;
}

void insertEnd(Node** head, int data) {
    Node* newNode = createEmptyNode();
    newNode->data = data;

    if ( (*head) == NULL) {
        (*head) = newNode;
        return;
    }

    Node* prevNode;
    prevNode = (*head);
    while (prevNode->next != NULL) 
        prevNode = prevNode->next;

    newNode->prev = prevNode;
    prevNode->next = newNode;
}

int main() {
    Node* head;
    head = NULL;

    Node* music01 = createEmptyNode();
    music01->data = 1;
    music01->prev = head;
    head = music01;

    Node* music02 = createEmptyNode();
    music02->data = 2;
    music02->prev = music01;
    music01->next = music02;


    Node* music03 = createEmptyNode();
    music03->data = 3;
    music03->prev = music02;
    music02->next = music03;
    

    Node* nodeIterator = calloc(1, sizeof(Node));
    nodeIterator = head;
    while (nodeIterator != NULL) {
        printf("%d\n", nodeIterator->data);
        nodeIterator = nodeIterator->next;
    }

    insertAtBeginning(&head, 5);

    printf("\nInsert at beginning\n");
    nodeIterator = head;
    while (nodeIterator != NULL) {
        printf("%d\n", nodeIterator->data);
        nodeIterator = nodeIterator->next;
    }

    insertAfter(music02, 4);

    printf("\nInsert After 2\n");
    nodeIterator = head;
    while (nodeIterator != NULL) {
        printf("%d\n", nodeIterator->data);
        nodeIterator = nodeIterator->next;
    }

    insertEnd(&head, 10);

    printf("\nInsert End 10\n");
    nodeIterator = head;
    while (nodeIterator != NULL) {
        printf("%d\n", nodeIterator->data);
        nodeIterator = nodeIterator->next;
    }

    return 0;
}