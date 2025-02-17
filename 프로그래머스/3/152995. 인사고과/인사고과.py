# 1.근무태도 + 동료 평가 점수 기록
# 다른 사원보다 두 점수가 모두 낮은 경우 1번 이상 -> 인센티브 x
# 한번도 없는 사원에 대해 -> 두 점수 합 높은 순 인센티브 차등 지급
# 등수 동일 -> 동석차 , 동석차 수 만큼 다음 석차는 건너 뜀!!!!!

# 0번째 인덱스(원호) 석차를 출력하라
# 인센티브를 받지 못하는 경우 -1

# 알아야 할 정보
# 1. 인센티브를 누가,몇명이 받을 수 있는가 (이중반복문.. ?..)
# 2. 인센티브를 받는 자들의 석차는 -> (인덱스, 합) 리스트 추가 후 정렬?
def solution(scores):
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a + target_b

    # 첫번째 점수에 대해서 내림차순,
    # 첫 번째 점수가 같으면 두 번째 점수에 대해서 오름차순으로 정렬합니다.
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0
    
    for a, b in scores:
        if target_a < a and target_b < b:
            return -1
        
        if b >= maxb:
            maxb = b
            if a + b > target_score:
                answer += 1
#     target_a, target_b = scores[0] # 완호 점수
#     target_score = target_a + target_b # 완호 점수 합
    
#     # 근무태도는 내림차순, 동료평가는 오름차순으로 정렬한다.
#     scores.sort(key = lambda x : (-x[0],x[1]))
    
#     maxb = 0
    
#     for a, b in scores:
#         # 완호가 인센티브를 받지 못하는 경우(한 번이라도 둘 다 작은 경우)
#         if target_a < a and target_b < b:
#             return -1
#         # a는 무조건 다음이 작으니, b만 확인해주면 된다.
#         # 갱신된 maxb보다 작으면, 인센티브 제외 -> 인센티브 받는 사람 골라내는 작업
#         if b >= maxb:
#             mavb = b
#             # 인센티브 받는 건에 대해선 원호보다 점수가 큰 경우만 확인하면된다. 
#             if a + b > target_score:
#                 # 완호 등수가 밀림(클때만 밀리면 동석차로 계산된)
#                 answer += 1
    
    
    
    return answer+1