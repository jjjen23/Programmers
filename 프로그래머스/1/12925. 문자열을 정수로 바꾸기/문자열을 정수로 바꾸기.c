#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* s) {
    int answer = 0;
    int sign = 1;
    
    if (s[0] == '-'){
        sign = -1;
        s++; //포인터 이동
    } else if (s[0]=='+') {
        s++; //포인터 이동
    }
    
    answer = sign * atoi(s);
    
    return answer;
}