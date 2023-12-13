#include<stdlib.h>
#include<math.h>
#include<stdio.h>
#include<assert.h>
#include<stdbool.h>
#include "lcm.h"

typedef struct Fraction {
    int numerator;
    int denominator;
} Fraction;

Fraction* createFraction(int numerator, int denominator) {
    Fraction* newFraction = (Fraction *)calloc(1, sizeof(Fraction));

    newFraction->numerator = numerator;
    newFraction->denominator = denominator;

    return newFraction;
}

float realValue(Fraction *fraction) {
    return (float)fraction->numerator / fraction->denominator;
}

Fraction* add(Fraction *fraction1, Fraction *fraction2) {
    bool areCommonDenominatorDifferent = fraction1->denominator != fraction2->denominator;
    int numerator = fraction1->numerator + fraction2->numerator;
    int commonDenominator = fraction1->denominator;

    if ( areCommonDenominatorDifferent ) {
        commonDenominator = lcm(fraction1->denominator, fraction2->denominator);
        int num1Transformed = (int)(commonDenominator / fraction1->denominator) * fraction1->numerator;
        int num2Transformed = (int)(commonDenominator / fraction2->denominator) * fraction2->numerator;
        numerator = num1Transformed + num2Transformed;
    }

    return createFraction(numerator, commonDenominator);
}

Fraction* sub(Fraction *fraction1, Fraction *fraction2) {
    bool areCommonDenominatorDifferent = fraction1->denominator != fraction2->denominator;
    int numerator = fraction1->numerator - fraction2->numerator;
    int commonDenominator = fraction1->denominator;

    if ( areCommonDenominatorDifferent ) {
        commonDenominator = lcm(fraction1->denominator, fraction2->denominator);
        int num1Transformed = (int)(commonDenominator / fraction1->denominator) * fraction1->numerator;
        int num2Transformed = (int)(commonDenominator / fraction2->denominator) * fraction2->numerator;
        numerator = num1Transformed - num2Transformed;
    }

    return createFraction(numerator, commonDenominator);
}

Fraction* multiply(Fraction *fraction1, Fraction *fraction2) {
    int numerator = fraction1->numerator * fraction2->numerator;
    int denominator = fraction1->denominator * fraction2->denominator;

    return createFraction(numerator, denominator);
}

Fraction* divide(Fraction *fraction1, Fraction *fraction2) {
    Fraction* invertedSecondFraction = createFraction(fraction2->denominator, fraction2->numerator);

    return multiply(fraction1, invertedSecondFraction);
}

void printFraction(Fraction *fraction) {
    printf(
        "Fraction(\n   numerator: %d, \n   denominator: %d\n)\n", 
        fraction->numerator, 
        fraction->denominator
    );
}

int main() {
    Fraction* frac1 = createFraction(10, 20);
    Fraction* frac2 = createFraction(5, 5);

    float valueF1 = realValue(frac1);
    printf("The real value of frac1 is: %.1f\n", valueF1);
    assert(valueF1 == 0.500000);

    float valueF2 = realValue(frac2);
    printf("The real value of frac2 is: %f\n", valueF2);
    assert(valueF2 == 1.000000);

    Fraction* sumOf1By2 = add(frac1, frac2);
    assert(sumOf1By2->numerator == 30 && sumOf1By2->denominator == 20);
    printf("\nSum of frac1 and frac2 results in: ");
    printFraction(sumOf1By2);

    Fraction* subOf1By2 = sub(frac1, frac2);
    assert(subOf1By2->numerator == -10 && subOf1By2->denominator == 20);
    printf("\nSub of frac1 and frac2 results in: ");
    printFraction(subOf1By2);

    Fraction* multOf1By2 = multiply(frac1, frac2);
    assert(multOf1By2->numerator == 50 && multOf1By2->denominator == 100);
    printf("\nSub of frac1 and frac2 results in: ");
    printFraction(multOf1By2);

    return 0;
}