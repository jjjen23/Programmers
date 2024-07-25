L = [1,4,7]
R = [3,6,9]
M = [2,5,8,0]

dict = {
    0 : [0,4,3,4,3,2,3,2,1,2],
    1 : [4,0,1,2,1,2,3,2,3,4],
    2 : [3,1,0,1,2,1,2,3,2,3],
    3 : [4,2,1,0,3,2,1,4,3,2],
    4 : [3,1,2,3,0,1,2,1,2,3],
    5 : [2,2,1,2,1,0,1,2,1,2],
    6 : [3,3,2,1,2,1,0,3,2,1],
    7 : [2,2,3,4,1,2,3,0,1,2],
    8 : [1,3,2,3,2,1,2,1,0,1],
    9 : [2,4,3,2,3,2,1,2,1,0],
    '*': [1,3,4,5,2,3,4,1,2,3],
    '#': [1,5,4,3,4,3,2,3,2,1]  
}

def solution(numbers, hand):

        
    answer = ''
    
    # 초기설정
    lefthand = '*'
    righthand = '#'
    
    for num in numbers:
        if num in L:
            answer += "L"
            lefthand = num
    
        elif num in R:
            answer += "R"
            righthand = num

        elif num in M:
            rightdistance = dict[righthand][num]
            leftdistance = dict[lefthand][num]
            
            # 만일 거리가 같다면, answer+=hand
            if rightdistance == leftdistance:
                if hand == "right":
                    answer += 'R'
                    righthand = num
                else:
                    answer += 'L'
                    lefthand = num
                # 해당 손위치 갱신
            else:
                if rightdistance < leftdistance:
                    answer+= 'R'
                    righthand = num
                else:
                    answer+= 'L'
                    lefthand = num
                
    return answer