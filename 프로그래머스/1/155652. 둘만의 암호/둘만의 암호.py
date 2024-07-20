apb = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def solution(s, skip, index):
    answer = ''
    for i in skip:
        apb.remove(i)
        
    n = len(apb)
    
    #s =list(s)
    
    for i in s:
        index_i = apb.index(i)
        answer += apb[(index_i+index)%n]
    
    
    return answer