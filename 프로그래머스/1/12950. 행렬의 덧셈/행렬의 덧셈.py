def solution(arr1, arr2):
    rows = len(arr1)
    colums = len(arr1[0])
    answer = [[0 for i in range(colums)] for i in range(rows)]
    for i in range(rows):
        for j in range(colums):
            answer[i][j] = arr1[i][j] + arr2[i][j]
            
    return answer