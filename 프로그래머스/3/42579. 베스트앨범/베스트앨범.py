def solution(genres, plays):
    answer = []
    
    # 가장 많이 재생된 장르 먼저(장르별 합)
    # 장르 내 많이 재생된 노래 먼저
    # 장르 내 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래 먼저
    # 딕셔너리 구조 => 고유번호 : {고유번호, 장르, 재생횟수}
    
    dict1 = {}
    dict_g = {}
    
    for i in range(len(genres)):
        dict1[i] = [i, genres[i], plays[i]]
    
    # 2번 기준, 3번 기준으로 정렬 
    sorted_dict = dict(sorted(dict1.items(), key=lambda x: (-x[1][2],x[1][0])))
    
    # print(sorted_dict)
    
    # 1번 기준 정렬해서 따로 딕셔너리 담기
    for key in dict1:
        g = dict1[key][1]
        p = dict1[key][2]
        
        if g not in dict_g:
            dict_g[g] = p
        else:
            dict_g[g] += p
    
    # 1번 기준으로 내림차순 정렬
    sorted_dict_g = sorted(dict_g.items(), key = lambda x : -x[1])
    
    
    # 1번 기준 검사 -> 장르별 2개씩 2번 3번 기준으로 정렬된 딕셔너리에서 뽑기
    for g, _ in sorted_dict_g:
        count = 0
        for k, v in sorted_dict.items():
            if g == v[1]:
                count += 1
                if count > 2:
                    break
                else:
                    # 각 장르별 최상위 2개씩 정답에 추가
                    answer.append(v[0])
            
    
    return answer