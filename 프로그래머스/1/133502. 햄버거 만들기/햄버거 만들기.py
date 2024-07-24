# 빵:1, 야채:2, 고기:3
hamberger = [1,2,3,1]
def solution(ingredient):
    answer = 0
    
    wowlist = []
    
    for i in ingredient:
        wowlist.append(i)
        if wowlist[-4:] == hamberger:
            answer += 1
            del wowlist[-4:]
        
    
    
            
    return answer