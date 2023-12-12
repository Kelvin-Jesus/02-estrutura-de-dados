#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<assert.h>

typedef struct Point {
    int x;
    int y;
} Point;

Point* initPoint(int x, int y) {
    Point *newPoint = (Point *)malloc(sizeof(Point));

    newPoint->x = x;
    newPoint->y = y;

    return newPoint;
}

int* access(Point *point) {
    int* points = malloc(sizeof(int) * 2);

    points[0] = point->x;
    points[1] = point->y;

    return points;
}

void setPoint(Point *point, int newX, int newY) {
    point->x = newX;
    point->y = newY;
}

float distanceBetween(Point *point1, Point *point2) {
    float deltaXSquared = pow(point1->x - point2->x, 2);
    float deltaYSquared = pow(point1->y - point2->y, 2);

    return sqrt(deltaXSquared + deltaYSquared);
}

void printOutPoint(Point *point) {
    printf("( X: %d, Y: %d )\n", point->x, point->y);
}

int main() {
    Point *point1, *point2;

    point1 = initPoint(10, 0);
    point2 = initPoint(10, 0);

    assert(point1->x == 10);
    assert(point1->y == 0);
    assert(point2->x == 10);
    assert(point2->y == 0);
    
    setPoint(point1, 3, 4);
    printOutPoint(point1);

    setPoint(point2, 10, 5);
    printOutPoint(point2);

    printf("( X: %d )\n", access(point1)[0]);
    
    printf("%f\n", distanceBetween(point1, point2));
}
