def solution(want, number, discount):
    answer = 0
    
    wantdict = {}
    for i in range(len(number)):
        wantdict[want[i]] = number[i]
    
    #print(wantdict)
    
    day=len(discount) - 10
    
    for i in range(day+1):
        tem = discount[i:i+10]
        #print(tem)
        judge = True
        for w in want:
            if wantdict[w] > tem.count(w):
                judge = False
                break
        if judge == True:
            #print(i)
            answer += 1
        

    return answer