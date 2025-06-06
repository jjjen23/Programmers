def solution(arr1, arr2):
    answer = 0
    # 배열의 길이가 긴 쪽이 더 크다
    # 길이가 같다면 각 배열에 있는 모든 원소 합을 비교해서 큰 쪽이 크고 같다면 같다.
    # arr2가 크면 -1 arr1가 크면 1 같다면 0
    
    if len(arr1) == len(arr2):
        if sum(arr1) == sum(arr2):
            return 0
        elif sum(arr1) > sum(arr2):
            return 1
        else:
            return -1
    else:
        if len(arr1) > len(arr2) :
            return 1
        else:
            return -1
