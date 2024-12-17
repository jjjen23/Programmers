def solution(triangle):
    answer = 0
    # print(dp[0])
    
    # 그냥 깊이 끝까지 탐색해서 마지막에 max를 구해야 함
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            # 왼쪽 끝일 때
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            # 오른쪽 끝일 때
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][-1]
            # 그 사이 일때(겹치니까 둘 중 큰거 선택)
            else:
                triangle[i][j] += max(triangle[i-1][j] , triangle[i-1][j-1])
            
            
    answer = max(triangle[-1])
    return answer