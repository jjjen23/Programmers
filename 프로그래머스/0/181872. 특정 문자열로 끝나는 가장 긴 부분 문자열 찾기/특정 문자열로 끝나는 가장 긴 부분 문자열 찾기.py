def solution(myString, pat):
    answer = ''
    res_idx = 0
    for i in range(0,len(myString)):
        # print(myString[i:i+len(pat)])
        if myString[i:i+len(pat)] == pat:
            # print(myString[i:i+len(pat)])
            res_idx = i+len(pat)
    
    answer = myString[:res_idx]
    return answer