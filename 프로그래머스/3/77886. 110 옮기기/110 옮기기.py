# '110'을 뽑아서.. 움직여서 사전순으로 가장 빠른 놈으로 만들라
# 사전순으로 가장 빨라질때까지 바뀐 위치에서 110을 계속 움직일 수 있다.
# 110보다 사전순으로 뒤에 있는 세 자리수는 111뿐이다.
# 가장 왼쪽에있는 111을 110으로 바꿔주는 것이 유리할 것이다.

# 풀이 전략 -> 존재하는 110을 전부 제거한다. , 어떤 위치에 110을 삽입해도 그로인해 새로운 110이 나타나는 경우는 없다.
# 110이 전부제거된 x의 오른쪽부터 탐색해서 첫번째 0 뒤에 110을 삽입해주면 된다.
# 제거시 나타나는 110도 전부 제거해준다고 생각하면 된다.

def solution(s):
    answer = []
    
    for one in s:
        stack = []
        cnt_110 = 0
        idx = 0
        
        while idx < len(one):
            # 0인 경우 체크
            if one[idx] == '0':
                # 만일 110인경우 110제거, 카운트
                if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1':
                    stack.pop()
                    stack.pop()
                    cnt_110 += 1
                    idx += 1 #스택에 넣지 않고 그냥 뛰어넘기
                    
                # 110이 아닌 경우
                else:
                    stack.append(one[idx])
                    idx += 1
            # 1인 경우
            else:
                stack.append(one[idx])
                idx += 1
                    
        # 다시 오른쪽 부터 탐색해서 cnt만큼 0 뒤에 삽입해준다.
        stack = ''.join(stack[::-1]) #뒤집어서 탐색
        idx_zero = stack.find('0') # 0이 있으면 해당인덱스를, 없으면 -1 반환 # 첫번째로 등장한느 0의 인덱스를 반환함
        
        if idx_zero != -1:
            res = stack[:idx_zero]+'011'*cnt_110+stack[idx_zero:]
        # 없으면 그냥 맨 앞에 붙인다.
        else:
            res = stack + '011'*cnt_110
            
        answer.append(res[::-1])

                    
    
    return answer