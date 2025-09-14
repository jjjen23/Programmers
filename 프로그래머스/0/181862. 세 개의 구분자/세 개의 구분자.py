def solution(myStr):
    answer = []
    for s in myStr:
        if s in ['a','b','c']:
            myStr = myStr.replace(s,' ')
                                  
    answer = myStr.split()
    
    if len(answer) == 0:
        return ["EMPTY"]
        
    return answer