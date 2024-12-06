# def solution(n):
#     if n % 2 != 0: return 0
#     p = n // 2
#     print(max(p, 0))
#     answer = [1, 3, 11]
#     for i in range(p - 2):
#         answer.append((4 * answer[-1] - answer[-2]) % 1000000007)
#         #p_sum = sum(answer[:-1])
#         #answer.append((3 * answer[-1] + 2 * p_sum) % 1000000007)
#     if n == 2:
#         return answer[1]
#     else:
#         return answer[-1]

def solution(n):
    
    if n % 2 != 0: return 0
    idx = n // 2
    answer = [1,3,11]
    if idx < 3 : return answer[idx]
    
    answer = [1,3,11]
    
    for i in range(3, idx+1):
        answer.append(4*answer[i-1]-answer[i-2])
    
    
    return answer[idx]%1000000007