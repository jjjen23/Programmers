# 어짜피 갱신에 필요한 것은 1의 갯수

def solution(s):
    answer = []
    # 길이를 2진법으로 표현
    bincnt = 0
    delzerocnt = 0
    while s != "1":
        zerocnt = s.count("0")
        delzerocnt += zerocnt
        #s = s.replace('0', '', zerocnt)
        onecnt=s.count("1")
        s = bin(onecnt)[2:]
        bincnt += 1
    
    # print(s)
    # print(bin(4)[2:])
    return [bincnt,delzerocnt]