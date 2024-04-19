#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<assert.h>

typedef int dataType;

typedef struct Node {
    dataType data;
    struct Node *leftNode, *rightNode;
} Node;

typedef struct {
    Node *root;
} Tree;

Tree* newTree() {
    Tree *tree = (Tree *)calloc(1, sizeof(Tree));

    return tree;
}

void destroy(Node *root) {
    if (root != NULL){
        destroy(root->leftNode);
        destroy(root->rightNode);
        free(root);
    }
}

bool isEmpty(Tree *tree) {
    assert(tree != NULL);
    if (tree->root == NULL || tree->root == 0) {
        return true;
    }

    return false;
}

Node* newNode(dataType data) {
    Node *newNode = (Node *)calloc(1, sizeof(Node));
    newNode->data = data;

    return newNode;
}

void insertRight(Tree *tree, dataType newValue, Node *fatherNode) {
    Node* node = newNode(newValue);

    if (isEmpty(tree)) {
        tree->root = node;
        return;
    }

    fatherNode->rightNode = node;
}

void insertLeft(Tree *tree, dataType newValue, Node *fatherNode) {
    Node* node = newNode(newValue);

    if (isEmpty(tree)) {
        tree->root = node;
        return;
    }

    fatherNode->leftNode = node;
}

int height(Node treeRoot) {
    return 0;
}

int main() {
    Tree *tree = newTree();
    printf("%d\n", isEmpty(tree));

    tree->root = newNode(10);
    printf("%d\n", isEmpty(tree));

    insertRight(tree, 20, tree->root);
    insertLeft(tree, 50, tree->root->rightNode);
    insertLeft(tree, 5, tree->root);

    destroy(tree->root);
    if (isEmpty(tree)) {
        printf("%s\n", "Árvore está vazia!");
    }

    return 0;
}
