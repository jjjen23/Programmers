# 1. 국어 점수 감소하는 순서
# 2. 국어 점수 같으면 영어 점수 증가하는 순서
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서

# 정렬 후 N줄에 걸쳐 각 학생의 이름을 출력한다.

n = int(input())
studList = []
for i in range(n):
    studList.append(list(input().split()))

studList.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in range(len(studList)):
    print(studList[i][0])