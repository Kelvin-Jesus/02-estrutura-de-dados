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

    printf("valor No anterior%d\n", prevNode->data);
    printf("valor No proximo%d\n", prevNode->next->data);
    newNode->next = prevNode->next;
    prevNode->next = newNode;
    newNode->prev = prevNode;

    printf("\nvalor No anterior%d\n", prevNode->data);
    printf("valor atual%d\n", newNode->data);
    printf("valor No proximo%d\n", newNode->next->data);

    if (newNode->next != NULL) 
        prevNode->next->prev = newNode;

    printf("\nvalor No anterior%d\n", prevNode->data);
    printf("valor atual%d\n", newNode->data);
    printf("valor No proximo%d\n", newNode->next->data);
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

void removeNode(Node** head, Node* nodeToDelete) {
    if (*head == NULL || nodeToDelete == NULL) {
        printf("Linked List is empty");
        return;
    }

    if (*head == nodeToDelete) {
        *head = nodeToDelete->next;
    }

    if (nodeToDelete->next != NULL) 
        nodeToDelete->next->prev = nodeToDelete->prev;

    if (nodeToDelete->prev != NULL)
        nodeToDelete->prev->next = nodeToDelete->next;

    free(nodeToDelete);
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

    // removeNode(&head, music03);

    printf("\nRemove Node 3\n");
    nodeIterator = head;
    while (nodeIterator != NULL) {
        printf("Nó Atual %d\n", nodeIterator->data);
        if ( nodeIterator->prev != NULL)
            printf("Nó Anterior %d\n", nodeIterator->prev->data);
        if ( nodeIterator->next != NULL)
            printf("Próximo Nó %d\n", nodeIterator->next->data);

        printf("\n");
        nodeIterator = nodeIterator->next;
    }

    return 0;
}