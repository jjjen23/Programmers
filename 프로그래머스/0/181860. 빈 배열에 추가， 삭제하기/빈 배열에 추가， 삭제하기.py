def solution(arr, flag):
    answer = []
    # true라면 리스트 뒤에 arr[i]를 arr[i]*2번 추가
    for i in range(len(flag)):
        if flag[i]:
            for _ in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                answer.pop()

    # False라면 리스트의 마지막 arr[i]개의 원소를 제거 하고 배열 반환
    return answer