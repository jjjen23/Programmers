def solution(my_string, m, c):
    answer = my_string[c-1:len(my_string):m]
    return answer