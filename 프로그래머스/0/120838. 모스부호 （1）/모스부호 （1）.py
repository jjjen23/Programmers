def solution(letter):
    answer = ''
    
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}   
    # 모스 부호는 공백으로 나누어져있고 시작과 끝에는 공백이 없다.
    
    letterList = letter.split()
    
    for letter in letterList:
        answer += morse[letter]
    
    return answer