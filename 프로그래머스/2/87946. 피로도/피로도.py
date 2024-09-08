from itertools import permutations 

def solution(k, dungeons):
    answer = -1

    
    for dungeon in permutations(dungeons , len(dungeons)):
            tem_k = k
            cnt = 0
            
            for i in dungeon:
                # 현재 피로도가 최소 피로도보다 크거나 같다면
                if i[0] <= tem_k:
                    tem_k -= i[1]
                    cnt += 1
                else:
                    break
            
            answer = max(answer, cnt)
            
    return answer