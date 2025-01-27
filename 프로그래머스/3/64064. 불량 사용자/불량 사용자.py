from itertools import product

def solution(user_id, banned_id):
    answer = 0
    candidate = []
    
    for ban in banned_id:
        temp = []
        for user in user_id:
            if len(user) == len(ban):
                flag = True
                for i in range(len(ban)):
                    if ban[i] != user[i] and ban[i] != '*':
                        flag = False
                        break
                if flag:
                    temp.append(user)
        candidate.append(temp)
    print(candidate)
    
    res = set()
    
    for p in product(*candidate):
        if len(set(p)) == len(banned_id):
            res.add(tuple(sorted(p)))
    print(res)
                
    answer = len(res)

    
    return answer