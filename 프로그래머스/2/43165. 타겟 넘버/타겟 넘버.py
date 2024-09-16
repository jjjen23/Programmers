def dfs(numbers, target, idx, values):
    global ans
    
    # 노드가 끝까지 간 상태고, 그 값이 타겟과 동일하면 +1
    if idx == len(numbers) and values == target:
        ans += 1
        return #1 더해 주고 종료
    
    # 끝 까지는 왔는데, 타겟과 동일하지 않다면.. 
    elif idx == len(numbers):
        return #걍 종료
    
    # 트리의(노드가,idx) 끝이 아니라면, 재귀적으로 호출
    dfs(numbers, target, idx+1, values + numbers[idx])
    dfs(numbers, target, idx+1, values - numbers[idx])
    
def solution(numbers, target):
    global ans
    ans = 0
    dfs(numbers,target,0,0)
    
    return ans
    

"""
# bfs
def solution(numbers, target):
    answer = 0
    leaves = []
    
    for num in numbers:
        tem = []
        
        # 더하는 경우와 빼는 경우 두가지가 존재함
        for leaf in leaves:
            tem.append(leaf + num)
            tem.append(leaf - num)
        leaves = tem # 현 시점부로 두 리스트는 같은 리스트를 가리킴
    
    # 모든 경우의 수 계산 후 target과 같다면 +1 해주기
    for leaf in leaves:
        if leaf == target:
            answer += 1
        
    
    return answer
"""