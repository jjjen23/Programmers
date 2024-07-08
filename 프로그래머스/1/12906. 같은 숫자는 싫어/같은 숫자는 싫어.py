#import collections from deque

def solution(arr):
    # 앞 뒤로 비교 -> 다르것 정답리스트에 추가
    answer = [arr[0]] #첫번째 요소는 넣어두기(어짜피 정답 확정이니)
    for i in range(1,len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer