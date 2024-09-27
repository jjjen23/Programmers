#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(long long n) {
    long long answer = 0;
    long long int_val = (long long)sqrt(n);
    
    
    if((int_val * int_val) == n) {
        answer = (int_val+1) * (int_val+1);
    } else {
        answer = -1;
    }
    return answer;
}