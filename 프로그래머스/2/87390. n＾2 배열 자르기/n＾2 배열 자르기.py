def solution(n, left, right):
    answer = []
    # arr2 = [[0]*n for _ in range(n)]
    #print(arr2)
    
    # newarr = []
    
    # x or y값 중 더 큰 값이 arr[x][y] 의 값이 된다. (규칙) 
    # for i in range(n):
    #     for j in range(n):
    #         arr2[i][j] = max(i,j) + 1
    #     newarr += arr2[i]
    #print(arr2)
    
    # newarr = []
    # for i in range(n):
    #     newarr += arr2[i]
    
#     print(newarr)
    
#     answer = newarr[left:right+1]

#     print(answer)
    
    # x or y값 중 더 큰 값이 arr[x][y] 의 값이 된다. (규칙) 
    # 범위 까지의 값을 행, 열로 재편성해서 값을 구한다. -> 시간 단축
    for i in range(left, right+1):
        row = i // n
        col = i % n
        answer.append(max(row,col)+1)
    
    return answer