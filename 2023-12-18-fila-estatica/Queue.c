#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_ELEMENTS 5

typedef struct Queue {
    int elements[MAX_ELEMENTS];
    int FRONT;
    int REAR;
} Queue;

void emptyQueue(Queue *queue) {
    queue->FRONT = -1;
    queue->REAR = -1;
}

bool isEmpty(Queue *queue) {
    if (queue->FRONT == -1) {
        return true;
    }

    return false;
}

bool isFull(Queue *queue) {
    if (queue->REAR == MAX_ELEMENTS - 1) {
        return true;
    }

    return false;
}

void enQueue(Queue *queue, int elementoToEnQueue) {
    if (isFull(queue)) {
        printf("\nQueue is Full!");
        return;
    }

    if (queue->FRONT == -1)
        queue->FRONT = 0;

    queue->REAR++;
    queue->elements[queue->REAR] = elementoToEnQueue;
}

void deQueue(Queue *queue) {
    if (isEmpty(queue)) {
        printf("\nQueue is empty!");
        return;
    }

    queue->FRONT++;
    if (queue->FRONT > queue->REAR) {
        emptyQueue(queue);
    }
}

void display(Queue *queue) {
    if (queue->REAR == -1) {
        printf("\nQueue is Empty!");
        return;
    }

    int i;
    printf("\nQueue elements are:\n");
    for (i = queue->FRONT; i <= queue->REAR; i++)
        printf("%d  ", queue->elements[i]);

    printf("\n");
}

int main() {
    Queue *queue = (Queue *)calloc(1, sizeof(Queue));
    emptyQueue(queue);

    //deQueue is not possible on empty queue
    deQueue(queue);

    //enQueue 5 elements
    enQueue(queue, 1);
    enQueue(queue, 2);
    enQueue(queue, 3);
    enQueue(queue, 4);
    enQueue(queue, 5);

    // 6th element can't be added to because the queue is full
    enQueue(queue, 6);

    display(queue);

    //deQueue removes element entered first i.e. 1
    deQueue(queue);

    //Now we have just 4 elements
    display(queue);

    return 0;
}