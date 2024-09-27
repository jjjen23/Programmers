#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num) {
    if(num==1){
        return 0;
    }
    
    int answer = 0;
    
    
    while (num != 1) {
        if (answer == 450) {
            return -1;
        }
        
        if (num%2 ==0){
            num /= 2;
            
        } else {
            num = num*3 + 1;

        }
        
        answer += 1;
    }
    
    return answer;
}