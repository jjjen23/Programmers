def solution(myString):
    answer = [ i for i in sorted(myString.split('x')) if i]
    return sorted(answer)