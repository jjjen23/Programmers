import math

def solution(n, stations, w):
    answer = 0
    
    start = 1
    for i in stations:
        end = i - w
        answer += math.ceil((end - start) / (2 * w + 1))
        start = i + w + 1

    answer += math.ceil((n + 1 - start) / (2 * w + 1))
    
    return answer

# import math

# # 5g W 전파 도달거리
# # 모든 아파트에 전파를 전달하기 위해 추가로 설치해야 할 기지국 최소

# def solution(n, stations, w):
#     answer = 0
    
#     # 방법1 : visited 배열을 만들어서 기존 설치된 전파 범위는 방문처리한다.(리스트에 추가)
#     #        w번째 인덱스부터 시작해서 끝까지 탐색 -> 방문하지 않음 -> 현재 인덱스 +w , -w까지 방문처리 -> 현재인덱스+w+1로 이동
#     #                                        -> 방문함 -> 인덱스 하나 이동
# .
    
    
#     # 답지 참고 코드: 필요한 기지국 수를 (아파트 길이 % 전파 범위)로 간단하게 측정
#     # 1부터 기지국 설치가 필요한 범위를 구해서 필요한 기지국 추가함
#     start = 1
#     for i in stations:
#         end = i-w
#         # 올림으로 하는 이유 : 1.xx 나오면 어짜피 기지국 2개 설치해야함 1개가지고 커버 안됨.
#         answer += math.ceil((end-start) / (2*w+1))
#         start = i + w + 1
        
#     answer += math.ceil((n-start+1) / (2*w+1))
            
    

#     return answer


# """
#     review: 처음 생각한 방법 -> 순차적으로 최소 기지국을 설치하려함, 그러나 최소라는 조건에 어긋나는 코드였다. -> 생각이 안남 -?> 답지참고-> 답지에서는 전파가 터지는 범위를 설치 구간 길이에 나누어 필요한 기지국 수를 찾음 -> 간단하고, 효율적인 방법..!!!!!
    
    
# """