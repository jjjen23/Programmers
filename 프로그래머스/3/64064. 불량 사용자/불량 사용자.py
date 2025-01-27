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
    
    res =set()
    
    for p in product(*candidate):
        if len(set(p)) == len(banned_id):
            res.add(tuple(sorted(p)))
    print(res)
                
    answer = len(res)
    
#     new_ban = []
    
#     total = []
#     dict1 = {}
#     # 제재 아이디 목록은 몇가지 경우의 수가 가능한지 리턴하시오!
#     # * ->를 .으로 변경
#     for id in banned_id:
#         tem = id.replace('*','.')
#         dict1[tem] = set()
#         new_ban.append(tem)
        
#     # print(dict1)
    
#     for banid in new_ban:
#         for userid in user_id:
#             if re.fullmatch(banid, userid):
#                 dict1[banid].add(userid)
                
#     print(dict1)
    
    
    
#     # print(new_ban)
    
#     setban = set(new_ban)
#     totalcom = []
    
#     for ban in setban:
#         cnt = new_ban.count(ban)
#         totalcom.append(list(combinations(dict1[ban],cnt)))
    
#     print(totalcom)
    
#     for i in totalcom:
#         answer *= len(i)
    
    return answer