# def solution(players, callings):
#     #answer = []
#     for name in callings:
#         i = players.index(name)
#         players[i], players[i-1] = players[i-1], players[i]
        
#     return players



def solution(players, callings):
    
    
    dict1 = {}
    for i in range(len(players)):
        dict1[players[i]] = i
        
    #answer = []
    
    for name in callings:
        idx = dict1[name]
        dict1[name] -=1
        dict1[players[idx-1]] +=1
        
        players[idx-1], players[idx] =  players[idx], players[idx-1]
    
    
    
    
    return players