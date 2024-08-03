def solution(today, terms, privacies):
    answer = []
    
    dict1 = {}
    
    
    for term in terms:
        k, v = term.split(" ")
        dict1[k] = int(v)
    
    for i in range(len(privacies)):
        
        nalja, alpa = privacies[i].split(" ")
        year, month, day = map(int, nalja.split("."))
        
        newday = day - 1
        daycarry = 0
        if newday == 0 :
            newday = 28
            daycarry = -1
            
        newmonth = (month + dict1[alpa]) + daycarry
        
        mcarry1 = 0
        if newmonth > 12 :
            mcarry1 = newmonth // 12
            newmonth = newmonth % 12
        
        mcarry2 = 0
        if newmonth == 0 :
            newmonth = 12
            mcarry2 = -1 
            
        newyear = year + mcarry1 + mcarry2
        
        #print(newyear, newmonth, newday)
        
        state = str(newyear) + f"{newmonth:02}" + f"{newday:02}"
        
        #print(state)
        today = ''.join(today.split("."))
        #print(today)
        
        # 파기할 정보 목록 
        if int(today) > int(state):
            answer.append(i+1)
        

        
    return answer