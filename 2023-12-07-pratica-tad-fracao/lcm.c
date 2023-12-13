#include "lcm.h"

int lcm(int n1, int n2) {
    int i, gcd, lcm;

    // loop to find the GCD
    for (i = 1; i <= n1 && i <= n2; ++i) {
        
        // check if i is a factor of both integers
        if (n1 % i == 0 && n2 % i == 0)
            gcd = i;
    }

    lcm = (n1 * n2) / gcd;
    
    return lcm;
}