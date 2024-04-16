#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<assert.h>

typedef int dataType;

typedef struct Node {
    dataType data;
    struct Node *leftNode;
    struct Node *rightNode;
} Node;

typedef struct {
    Node *root;
} Tree;

Tree* newTree() {
    Tree *tree = (Tree *)calloc(1, sizeof(Tree));

    return tree;
}

bool isEmpty(Tree *tree) {
   assert(tree != NULL);
   if (tree->root == NULL)
        return true;

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

    printf("%d\n", tree->root->rightNode->data);
    printf("%d\n", tree->root->leftNode->data);
    printf("%d\n", tree->root->rightNode->leftNode->data);

    return 0;
}
