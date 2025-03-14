# 열쇠로 좌물쇠를 열 수 있으면 true,없으면 false

# 좌물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 좌물쇠를 여는데 영향x -> 좌물쇠 원래크기 3배로 확장하고 그 가운데 원본을 둔다.

# 좌물쇠 영역 내에서는 열쇠의 돌기부분과 좌물쇠 홈부분이 정확히 일치해야함
# 좌물쇠의 모든 홈을 채워 비워있는 곳이 없어야, 열 수 있다.
# 0은 홈, 1은 돌기 부분
# 열쇠를 이리 저리 돌려서 좌물쇠 0 영역 == 열쇠 1 영역이 같으면 true다.
# key크기는 <= lock의 크기


# 1.key 회전 함수 (90, 270, 180)
def rotate(array , d):
    n = len(array)
    result = [[0]*n for _ in range(n)]
    
    # 90
    if d % 4 == 1:
        for i in range(n):
            for j in range(n):
                result[j][n-i-1] = array[i][j]
    # 180
    elif d %  4 == 2:
        for i in range(n):
            for j in range(n):
                result[n-i-1][n-j-1] = array[i][j]
    
    # 270
    elif d % 4 == 3:
        for i in range(n):
            for j in range(n):
                result[n-j-1][i] = array[i][j]
    
    # 0, 360 : 그대로
    else:
        return array
    
    return result

# 2. lock 열림 조건 확인 함수 -> lock과 key를 더해서 lock의 모든 원소가 1이면 오픈 가능
# 좌물쇠 중간 n*n부분이 모두 1인지 확인하는 함수
def check(new_lock):
    n = len(new_lock) // 3
    # 예를 들어, n=3이면 3~6까지 확인(중앙)
    for i in range(n, n*2):
        for j in range(n, n*2):
            if new_lock[i][j] != 1:
                return False
    return True #모든 영역 1일때만 True

def solution(key, lock):
    answer = True
    m = len(key)
    n = len(lock)
    # 기존 보다 3배 큰 좌물쇠
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    # 새로운 좌물쇠 중앙에 기존 좌물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
            
    # 열쇠를 (1,1)부터 (n*2-1, n*2-1)까지 이동시키며 확인
    for i in range(1, n*2):
        for j in range(1, n*2):
            # 열쇠를 0~270회전 시키며 확인
            for d in range(4):
                r_key = rotate(key, d)
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += r_key[x][y]
                # 열었다면!! 바로 정답 반환
                if check(new_lock):
                    return True
                # 못열었다면.. 더한거 빼주기
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= r_key[x][y]
    
    # 이까지 왔다면 못열었단 뜻이죠.
    return False

"""
    lock의 영역을 확장해서 가능한 모든 각도를 탐색하는 전수조사 방법이었다... 5중반복문일 줄은 몰랐는데..
    정답을 봤을때 코드 자체가 어렵지는 않았지만 스스로는 생각해내기 어려운 그런 아이디어랄까..
    일단 lock을 확장하는 것, 확장한 것에서 범위를 적절하게 설정해 열리는지 아닌지 탐색하는 과정이 어려웠던 것 같다. 
    
"""