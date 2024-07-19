def solution(lottos, win_nums):
    rank_dict = {
        6 : 1,  
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5,
        1 : 6
    }
    
    # 현재 일치하는 개수 n에 저장 -> 최저 순위 번호가 됨
    # 2개
    min_cnt = len(set(lottos) & set(win_nums)) 
    # 최고순위 : 1~45 중에 일단 n 에 있는 수 전부 제외, 0의 갯수 카운트, 
    zero_cnt = lottos.count(0)
    
    max_cnt = 0
    if zero_cnt<= 6-min_cnt:
        max_cnt = min_cnt+zero_cnt
    else:
        max_cnt = min_cnt+zero_cnt
    
      # max_cnt와 min_cnt가 rank_dict의 키로 사용될 수 있는지 확인 후 사용
    max_rank = rank_dict.get(max_cnt, 6)  # max_cnt가 rank_dict의 키로 없으면 기본값 6 사용
    min_rank = rank_dict.get(min_cnt, 6)  # min_cnt가 rank_dict의 키로 없으면 기본값 6 사용
    
    answer = [max_rank, min_rank]
    
    return answer