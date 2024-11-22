apbs = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def solution(name):
    answer = 0
    print(apbs[13],apbs[12])
    # A로 부터의 각 알파벳 최소 위치를 저장한다. a ~ n (0~13) z~o(1~12)
    apbdis = {}
    
    tem1 = 0
    for i in range(0,14):
        apbdis[apbs[i]] = tem1
        tem1 += 1
    tem2 = 12
    for i in range(14,26):
        apbdis[apbs[i]] = tem2
        tem2 -= 1
    # print(apbdis)
    
    # 전부 a면 0
    if list(name).count('A') == len(name):
        return 0
    # a면 커서 이동 +1
    # 나머지 알파벳이면 최소값 더해줌
    # 최소 이동 횟수 : 기존 저장 값 , 연속된 A의 왼쪽 시작, 연속된 A의 오른쪽 시작 중 최소값
    spell_move = 0
    cursor_move = len(name) - 1
    for i, spell in enumerate(name):
        spell_move += apbdis[spell]
        # 다음 인덱스로
        next = i+1
        # 다음 인덱스가 A면, 연속된 A수 카운트
        while next < len(name) and name[next] == 'A':
            next += 1
        cursor_move = min([cursor_move,2*i + (len(name)-next), i+2*(len(name)-next)])
        
    # 알파벳 최소 무브 + 커서 최소 무브
    answer = spell_move + cursor_move
        
        
    
    
    return answer