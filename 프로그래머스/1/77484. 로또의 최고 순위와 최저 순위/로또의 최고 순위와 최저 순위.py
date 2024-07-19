def solution(lottos, win_nums):
    rank_dict = {
        # 당첨 개수 : 등수
        6 : 1,  
        5 : 2,
        4 : 3,
        3 : 4,
        2 : 5,
        1 : 6,
        0 : 6
    }
    
    # 현재 일치하는 개수 n에 저장 -> 최저 순위 번호가 됨
    # 2개
    min_cnt = len(set(lottos) & set(win_nums)) 
    
    # 지워진거 카운트
    zero_cnt = lottos.count(0)
    
    max_cnt = min_cnt+zero_cnt
    
    max_rank = rank_dict[max_cnt] 
    min_rank = rank_dict[min_cnt]  
    
    answer = [max_rank, min_rank]
    
    return answer