def solution(k, ranges):
    answer = []
    points = []
    n = 0
    dp = []
    while k > 1:
        points.append(k)
        if k % 2 == 0:
            k //= 2
        else:
            k = k*3 + 1
        n += 1
    points.append(k)
    
    # n 값은 구함
    # print(n)
    # print(points)
    
    for i in range(1,len(points)):
        # 넓이 * (윗변+아랫변) * 0.5
        area = (i-(i-1))*(points[i]+points[i-1])*0.5
        # print(area)
        dp.append(area)
    # print(dp)
    
    for a1,b in ranges:
        sum = 0
        a2 = n+b
        # print(a1,a2)
        
        if a1 > a2 :
            answer.append(-1)
            continue
        # if a1 == a2:
        #     answer.append(0)
        #     continue
        for i in range(a1,a2):
            sum += dp[i]
        answer.append(sum)
        
    return answer