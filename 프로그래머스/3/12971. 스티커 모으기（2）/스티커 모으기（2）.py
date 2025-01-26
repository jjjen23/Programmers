def solution(sticker):
    answer = 0
    
    # 스티커 길이가 하나면 바로 그거 리턴하면 끝
    if len(sticker) == 1:
        return sticker.pop()
    
    d1, d2 = [0] * len(sticker), [0] * len(sticker)
    
    d1[0] = sticker[0]
    d1[1] = d1[0]
    
    # 1번 선택하는 경우
    for i in range(2, len(sticker)-1):
        d1[i] = max(d1[i-2]+sticker[i], d1[i-1])
    
    # 2번 선택하는 경우
    for i in range(1, len(sticker)):
        d2[i] = max(d2[i-2]+sticker[i], d2[i-1])
    
    return max(d1[-2], d2[-1])

#     size = len(sticker)
    
#     # 1번 선택하는 경우 -> 마지막 선택 불가
#     dp1 = [0] + sticker[:-1]
#     for i in range(2,size):
#         # 최대값(새로 들어온 수 + 2칸 전까지의 최적 값 , 1칸 전의 최적 값)
#         dp1[i] = max(dp1[i-1], dp1[i-2]+dp1[i])
        
    
    
#     # 2번 선택하는 경우 -> 첫번째 선택 불가
#     dp2 = [0] + sticker[1:]
#     for i in range(2,size):
#         dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])
    
#     answer = max(dp1[-1], dp2[-1])
    
    
    
    return answer