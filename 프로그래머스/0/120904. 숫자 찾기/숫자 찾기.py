def solution(num, k):

    strnum = list(str(num))
    
    if str(k) in strnum:
        
        return strnum.index(str(k))+1
    else:
        return -1