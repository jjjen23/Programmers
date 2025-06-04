def solution(arr, idx):
    answer = 0
    
    # idx보다 크면서 배열으 값이 1인 가장 작은 인덱스를 반환
    # 그런인덱스 없다면 -1 반환
    
    for i in range(idx, len(arr)):
        if arr[i]==1:
            return i
    return -1
        