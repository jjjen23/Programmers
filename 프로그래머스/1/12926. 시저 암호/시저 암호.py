lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
            
        elif 'a' <= i <= 'z':
            index = lower.index(i)
            answer += lower[(index+n)%26]
            
        elif 'A' <= i <= 'Z':
            index = upper.index(i)
            answer += upper[(index+n)%26]
    return answer