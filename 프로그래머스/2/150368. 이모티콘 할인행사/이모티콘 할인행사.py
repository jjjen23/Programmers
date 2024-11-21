from itertools import product

def solution(users, emoticons):
    totalres = []

    
    # 할인율은 10, 20, 30, 40 중 하나로 설정 
    # 최소 할인율보단 커도 될듯
    # users.sort(key = lambda x : x[0])
    # print(users)
    
    sales = [10,20,30,40]
    
    # while sales and users[0][0] > sales[0]:
    #     sales.pop(0)
    
    result = list(product(sales,repeat=len(emoticons)))
    
    # 할인율 당
    for perm in result:
        plus = 0
        money = 0
        # 사람 당
        for user in users:
            limit = user[1]
            wantsale = user[0]
            permoney = 0
            for i in range(len(perm)):
                if wantsale <= perm[i]:
                    permoney+=emoticons[i]*((100-perm[i])/100)
            if permoney >= limit:
                plus += 1
            else:
                money += permoney
        totalres.append((plus,money))
        
    # 1. 이모티콘 플러스 가입자 최대로
    # 2. 이모티콘 판매액 최대로
    totalres.sort(key=lambda x : (-x[0],-x[1]))  
    answer = list(totalres[0])
    return answer