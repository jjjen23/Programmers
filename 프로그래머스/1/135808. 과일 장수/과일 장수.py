def solution(k, m, score):
    answer = 0
    # 점수 리스트 오름차순 정렬
    score.sort(reverse = True)
    
    for i in range(0, len(score), m):
        Box = score[i : i+m]
        # print(min(Box))
        if len(Box) == m :
            answer += min(Box) * m
    return answer