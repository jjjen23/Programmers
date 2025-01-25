def solution(genres, plays):
    answer = []
    
    # 가장 많이 재생된 장르 먼저(장르별 합)
    # 장르 내 많이 재생된 노래 먼저
    # 장르 내 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래 먼저
    # 딕셔너리 구조 => 고유번호 : {장르, 재생횟수}
    
    dict1 = {}
    dict_g = {}
    
    for i in range(len(genres)):
        dict1[i] = [i, genres[i], plays[i]]
    
    sorted_dict = dict(sorted(dict1.items(), key=lambda x: (-x[1][2],x[1][0])))
    
    print(sorted_dict)
    
    for key in dict1:
        g = dict1[key][1]
        p = dict1[key][2]
        
        if g not in dict_g:
            dict_g[g] = p
        else:
            dict_g[g] += p
    

    sorted_dict_g = sorted(dict_g.items(), key = lambda x : -x[1])
    
    for g, _ in sorted_dict_g:
        count = 0
        for k, v in sorted_dict.items():
            if g == v[1]:
                count += 1
                if count > 2:
                    break
                else:
                    answer.append(v[0])
            
    
    return answer