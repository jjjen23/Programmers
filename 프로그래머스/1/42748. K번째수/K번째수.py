def solution(array, commands):
    answer = []
    for arr in commands:
        tem = []
        for i in range(arr[0]-1, arr[1]):
            tem.append(array[i])
        tem.sort()
        answer.append(tem[arr[2]-1])
    return answer