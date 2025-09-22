# BOJ 3190 뱀

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

# 동(우), 남(하), 서(좌), 북(상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 사과 위치 기록
for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1  # 사과는 1로 표시

# 방향 변환 정보
l = int(input())
moves = []
for _ in range(l):
    x, c = input().split()
    moves.append([int(x), c])  # (시간, 방향)

def turn(direction, c):
    if c == 'L':  # 왼쪽 90도
        return (direction - 1) % 4
    else:  # 오른쪽 90도
        return (direction + 1) % 4

def simulate():
    r, c = 0, 0 # 시작 위치
    graph[r][c] = 2  # 뱀 위치는로 표시
    direction = 0  # 처음엔 동쪽(→)
    time = 0
    index = 0

    snake = [(r, c)]  # 뱀의 몸 위치(꼬리부터)

    while True:
        # 방향전환이 없다면 그냥 나아가
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 범위 안이고 자기 몸에 부딪히지 않은 경우
        if 0 <= nr < n and 0 <= nc < n and graph[nr][nc] != 2:
            if graph[nr][nc] == 1:  # 사과가 있으면
                graph[nr][nc] = 2 # 머리 이동-> 뱀으로 덮어쓰니까 사과를 굳이 0으로 초기화할 필요가 없다.
                snake.append((nr, nc)) # 이동한 머리추가, 꼬리는 움직이지 않으므로 그대로
            else:  # 빈칸이면 몸 삭제없음
                graph[nr][nc] = 2 # 한칸 이동한 곳이 머리고
                snake.append((nr, nc)) # 추가해준다.
                pr, pc = snake.pop(0)  # 꼬리 부분 제거
                graph[pr][pc] = 0 # 뱀의 일부가 아니므로 0으로 초기화해준다.

        else:  # 벽이나 자기 몸과 부딪히면 종료
            time += 1
            break

        r, c = nr, nc # 좌표 갱신
        time += 1 # 갱신할 때 마다 +1씩!

        # 방향 전환 (해당 초가 끝난 뒤 적용)
        if index < l and time == moves[index][0]:
            direction = turn(direction, moves[index][1])
            index += 1

    return time

print(simulate())