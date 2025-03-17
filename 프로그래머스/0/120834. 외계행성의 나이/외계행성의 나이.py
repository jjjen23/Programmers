def solution(age):
    answer = ''
    start = 97
    dict1 = {}
    for i in range(0,26):
        dict1[i] = chr(start)
        start += 1
    

    ageL = list(str(age))
    for a in ageL:
        a = int(a)
        answer += dict1[a]
        
    return answer