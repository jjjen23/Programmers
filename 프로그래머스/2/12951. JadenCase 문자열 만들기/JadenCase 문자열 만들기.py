def solution(s):
    answer = ''
    words = s.split(" ")
    
    print(words)
    print(words[0][0])
    
    for i in range(len(words)):
        for j in range(len(words[i])):
            if j == 0:
                answer += words[i][j].upper()
            else:
                answer += words[i][j].lower()
        if i != len(words)-1:
            answer += " "
        
    
    
    
    return answer