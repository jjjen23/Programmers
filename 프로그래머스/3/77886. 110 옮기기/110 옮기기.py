# '110'을 뽑아서.. 움직여서 사전순으로 가장 빠른 놈으로 만들라
# 사전순으로 가장 빨라질때까지 바뀐 위치에서 110을 계속 움직일 수 있다.
# 110보다 사전순으로 뒤에 있는 세 자리수는 111뿐이다.
# 가장 왼쪽에있는 111을 110으로 바꿔주는 것이 유리

# 풀이 전략 -> 존재하는 110을 전부 제거한다, 어떤 위치에 110을 삽입해도 그로인해 새로운 110이 나타나는 경우는 없다.
# 110이 전부제거된 x의 오른쪽부터 탐색해서 첫번째 0 뒤에 110을 삽입해주면 된다. -> 남아있는 문자열에서 1은 우선순위가 가장 낮다고 생각하면 된다.
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
        # 오른쪽부터 가장 먼저 등장하는 0 오른편에 '110'을 넣어야 우선순위 충족 
        
        stack = ''.join(stack[::-1]) #뒤집어서 탐색
        idx_zero = stack.find('0') # 0이 있으면 해당인덱스를, 없으면 -1 반환 # 첫번째로 등장한느 0의 인덱스를 반환함
        
        if idx_zero != -1:
            res = stack[:idx_zero]+'011'*cnt_110+stack[idx_zero:]
        # 없으면 그냥 맨 앞에 붙인다.
        # 남아있는 문자열에서 1은 우선순위가 가장 낮다고 생각하면 된다.
        # 고로 남아있는 문자열이 1 뿐이라면 1 왼쪽에 '110'이 위치하도록해야함
        else:
            res = stack + '011'*cnt_110
        
        # 뒤집어서 정답에 추가
        answer.append(res[::-1])

                    
    return answer


"""
    review: 2진수의 특성을 잘 활용한 사람이 풀었을 문제, 이진수 값이 낮다 = 우선순위가 낮다. 3비트에서 110은 111다음 가장 우선순위가 높다는 점을 파악한 뒤, 추출한 110을 어디에 , 무엇을 기준을 배치해야하는지 생각해야 했던 문제이다. 
.. 또한 stack을 이용해 시간 복잡도 기준도 충족해주어야 통과할 수 있는 문제였다. 답지를 참고했지만 스택,인덱스를 활용해서 문자열, 배열을 다루는 방법에 익숙해지는 것이 좋을 것 같다.

"""