#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(int x) {
    bool answer = true;
    
    int tem = x;
    int sum = 0;
    
    while(tem > 0) {
        sum += tem % 10;
        tem /= 10;
    }
    
    if (x % sum != 0) {
        answer = false;
    }
    return answer;
}