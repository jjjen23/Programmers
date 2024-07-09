def solution(array, commands):
    answer = []
    
    for arr in commands:
        tem = []
        #인덱스 슬라이싱
        for i in range(arr[0]-1, arr[1]):
            tem.append(array[i])
        #슬라이싱한 리스트 정렬    
        tem.sort()
        #원하는 원소값 정답 리스트에 추가
        answer.append(tem[arr[2]-1])
        
    return answer