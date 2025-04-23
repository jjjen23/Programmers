# 강의실 배정 # 골드5 #그리디
import heapq
import sys
input = sys.stdin.readline
n = int(input())
st = []

for _ in range(n):
    ss, tt = map(int, input().split())
    st.append([ss,tt])

# 최소의 강의실을 사용해서 모든 수업을 가능하게 해야한다.
# 강의실 개수를 출력하라
# 이전 end와 새로운 start비교 및 갱신 필요
# 시작시간 기준 정렬
# 우선순위 큐 사용하여 강의 종료 시간 관리
# 가장 빨리 끝나는 강의실 종료 시간과 현재 강의의 시작 시간 비교
# 현재 강의의 시작 시간이 종료시간보다 크거나 같다면 재사용
# 아니라면 새로운 강의실 추가
# 우선순위 큐에 현재 강의 종료시간 추가
# 우선순위 큐 크기가 최소 강의실 수
# 힙을 사용하는 방법이있다늬..굿..!!!!

st.sort() #시작시간 오룸차순 정렬
rooms = []
heapq.heappush(rooms,st[0][1]) #첫 강의 종료시간 추가(최소힙, 오름차순)

for i in range(1,n):
    # 가장 빨리 끝나는 강의실 종료시간 확인
    if rooms[0] <= st[i][0]:
        heapq.heappop(rooms) #재사용
    heapq.heappush(rooms,st[i][1]) #종료시각 갱신 or 재사용안하면 새로운 종료시각 추가

print(len(rooms))





