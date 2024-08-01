dict1 = {
    1 : 3,
    2 : 2,
    3 : 1,
    4 : 0,
    5 : 1,
    6 : 2,
    7 : 3
}

dict2 = {
    "R" : 0,
    "T" : 0,
    "C" : 0,
    "F" : 0,
    "J" : 0,
    "M" : 0,
    "A" : 0,
    "N" : 0
}

def solution(survey, choices):
    # R, T, C, F, J, M, A, N = 0, 0, 0, 0, 0, 0, 0, 0
    
    answer = ''
    
    for i in range(len(survey)):
        if choices[i] < 4 :
            dict2[survey[i][0]] += dict1[choices[i]]
        if choices[i] > 4 :
            dict2[survey[i][1]] += dict1[choices[i]]
            
    
    if dict2['R'] >= dict2['T'] :
        answer += "R"
    else :
        answer += "T"
        
    if dict2['C'] >= dict2['F'] :
        answer += "C"
    else :
        answer += "F"
        
    if dict2['J'] >= dict2['M'] :
        answer += "J"
    else :
        answer += "M"
        
    if dict2['A'] >= dict2['N'] :
        answer += "A"
    else :
        answer += "N"  
    
    return answer