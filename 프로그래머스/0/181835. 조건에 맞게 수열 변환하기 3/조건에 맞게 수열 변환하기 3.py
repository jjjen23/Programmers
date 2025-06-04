def solution(arr, k):
    answer = []
    if k % 2 != 0:
        # 모든 원소에 k를 곱한다.
        return [i*k for i in arr]
    else:
        # 모든 원소에 k를 더한다.
        return [i+k for i in arr]