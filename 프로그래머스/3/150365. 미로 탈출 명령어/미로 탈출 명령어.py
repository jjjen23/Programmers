import sys
sys.setrecursionlimit(2600)

# 미로를 탈출하기 위한 경로를 출력하라.(사전순으로 가장 빠른 경로 출력, K회 이동가능 == 경로길이가 k여야함)
# 조건대로 미로 탈출안되는 경우 -> "impossible"출력

            
        
def solution(n, m, x, y, r, c, k):
    answer = ''
    direct = [['d',1,0],['l',0,-1],['r',0,1],['u',-1,0]] #미리 사전 순 배열하면 가장 빠르게 탐색 가능
    
    dist = abs(x-r) + abs(y-c)
    # 맨해튼 경로가 k보다 크면 애초에 조건 만족 x
    if dist > k:
        return "impossible"
    # dist(맨해튼경로가) k보다 작을때는 dist값과 k의 홀, 짝이 동일해야 조건을 충족할 수 있음. 
    if dist % 2 != k % 2 :
        return "impossible"
    
    
    # dfs함수는 조건을 만족하는 path를 반환하거나 그렇지 않을 경우 none을 반환한다. -> 즉, 반환하는 값은 조건 만족하는 path, none 중 하나이다.
    def dfs(cx,cy,path,cnt):
        # k를 만족하고, End 좌표에 도달했다면 경로 반환 
        if cnt == k :
            if cx == r and cy == c:
                return path
        # k를 만족하지 않았다면, 경로 탐색(사전 순 탐색)
        else:
            for d in direct:
                # 다음 좌표로 이동
                nx = cx + d[1]
                ny = cy + d[2]
                
                # 좌표 범위 만족하는지 검사
                if 1 <= nx <= n and 1 <= ny <= m:
                    # 현재 위치에서 end좌표 까지 맨해튼 거리 계산
                    dist = abs(nx - r) + abs(ny - c)
                    # 현재 위치에서 목표까지 맨해튼 거리가 남은 이동 횟수보다 크다면 더 이상 진행 불가하므로 다른 경로 탐색(상하좌우 탐색)
                    if dist > k - (cnt + 1):
                        continue
                    # 남은 이동 회수보다 맨해튼 거리가 작다면, 그 경로를 추가하고 다음으로 재귀
                    rtn = dfs(nx,ny,path+d[0],cnt+1)
                    
                    
                    # 사전순으로 가장 빠른 경로 찾자마자 반환하고 dfs종료하는 코드!
                    # 가장 먼저 k조건을 만족하며 end에 도달한 경로를 반환하여 종료한다.(사전순으로 탐색했기 때문에 첫번째 반환 값이 정답이다.)
                    if rtn is not None:
                        return rtn
        
    answer = dfs(x,y,"",0)
    
    if answer is None:
        return "impossible"
    
    return answer