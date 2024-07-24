def solution(X, Y):
    answer = ''
    
    sameSet = set(X) & set(Y)
    if len(sameSet) == 0:
        return "-1"
    
    result = []
    for i in sameSet:
            minvalue = min(X.count(i), Y.count(i))
            for _ in range(minvalue):
                result.append(i)    
            
                
    result.sort(reverse=True)
    if result[0] == '0' :
        return  '0'
    
    answer = ''.join(map(str,result))
    
    
#     X = list(X)
#     X.sort(reverse=True)
#     Y = list(Y)
    
#     for i in X :
#         if i in Y :
#             answer += i
#             Y.remove(i)
    
#     if len(answer) == 0:
#         return "-1"
#     if int(answer) == 0:
#         return "0"
    
    
    return answer
        
        
            