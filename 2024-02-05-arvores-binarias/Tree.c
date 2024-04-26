#include<stdlib.h>
#include<stdio.h>
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
    if (root != NULL) {
        destroy(root->leftNode);
        destroy(root->rightNode);
        free(root);
    }
}

void print(Node *root) {
    if (root == NULL) {
        printf("null");
        return;
    }

    printf("(");
    print(root->leftNode);
    printf(" %d ", root->data);
    print(root->rightNode);
    printf(")");
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

int height(Node *treeRoot) {
    if (treeRoot == NULL) {
        return -1;
    }

    int alturaSubArvoreDireita = 1 + height(treeRoot->rightNode);
    int alturaSubArvoreEsquerda = 1 + height(treeRoot->leftNode);

    if (alturaSubArvoreDireita > alturaSubArvoreEsquerda) {
        return alturaSubArvoreDireita;
    }

    return alturaSubArvoreDireita;
}

Node* searchNode(Node *treeRoot, dataType nodeData) {
    if (treeRoot == NULL) {
        return NULL;
    }

    if (treeRoot->data == nodeData) {
        return treeRoot;
    }

    if (searchNode(treeRoot->leftNode, nodeData) != NULL) {
        return treeRoot->leftNode;
    }

    return searchNode(treeRoot->rightNode, nodeData);
} 

int main() {
    Tree *tree = newTree();
    printf("%d\n", isEmpty(tree));

    tree->root = newNode(10);
    printf("%d\n", isEmpty(tree));

    insertRight(tree, 20, tree->root);
    insertLeft(tree, 50, tree->root->rightNode);
    insertLeft(tree, 5, tree->root);

    printf("%d", height(tree->root));
    printf("\n");
    print(tree->root);
    destroy(tree->root);
    if (isEmpty(tree)) {
        printf("%s\n", "Árvore está vazia!");
    } 

    return 0;
}
