def solution(numbers):
    answer = []
    
    # 가장 마지막에 등장하는 0을 찾아
    # 그 0을 1로 변경
    # 홀수의 경우 마지막 0 다음 인덱스는 0로 변경해줌(01->10)
    for num in numbers:
        
        bin_num = list('0'+bin(num)[2:])
        idx = ''.join(bin_num).rfind('0')
        bin_num[idx] = '1'
        
        if num % 2 == 1:
            bin_num[idx+1] = '0'
            
        answer.append(int(''.join(bin_num),2))
            

            
            
    return answer