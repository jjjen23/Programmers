def solution(data, col, row_begin, row_end):
    answer = 0
    # col 번째 컬럼 기준 오름차순, 동일할 시 첫번째 컬럼(기본키)내림차순 정렬
    data.sort(key=lambda x : (x[col-1],-x[0]))
    # print(data)
    
    # i번째 행 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지의 합 정의(row_begin-1, row_end)
    S_i = []
    for i in range(row_begin-1,row_end):
        sum = 0
        for ele in data[i]:
            sum += ele % (i+1)
        S_i.append(sum)
    # print(S_i)
    
    # bitwise xor
    while S_i:
        next = S_i.pop()
        answer = answer ^ next
    
    return answer