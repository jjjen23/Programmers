def solution(m, musicinfos):
    answer = ''
    # 1분에 하나씩 재생 됨
    # A#->a,B#->b,C#->c,D#->d,F#->f,G# -> g
    # 시간 확보 -> 시간이 멜로디 길이보다 길다면 악보 확장 -> m문자열이 있는지 검사 -> 맞다면 제목 출력
    
    
    replacements = {
        'A#' : 'a',
        'B#' : 'b' ,
        'C#' : 'c' ,
        'D#' : 'd' ,
        'F#' : 'f' ,
        'G#' : 'g' ,
        'E#' : 'e'
        
    }
    
    for old, new in replacements.items():
        m = m.replace(old, new)
    
    sortMusicinfo = []
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        start_hh,start_mm  = start.split(':')
        start_time = int(start_hh)*60 + int(start_mm)
        end_hh, end_mm = end.split(':')
        end_time = int(end_hh)*60 + int(end_mm)
        runnigTime = end_time-start_time
        
        for old, new in replacements.items():
            melody = melody.replace(old,new)
        
        melody = list(melody)
        
        if runnigTime > len(melody) :
            melody = (melody * (runnigTime // len(melody) + 1))[:runnigTime]
        
        else:        
            melody = melody[:runnigTime]
            
        melody = ''.join(melody)
        
        
        sortMusicinfo.append([runnigTime,title,melody])
    
    sortMusicinfo.sort(key = lambda x : -x[0])
    
    
    # print(sortMusicinfo)
    
            
    # 큰 거 + 입력순서대 검사해서 먼저 정답인거 반환
    for info in sortMusicinfo:
        if m in info[2]:
            answer = info[1]
            break
    
    
    if len(answer) == 0 :
        return "(None)"
# 끝 샵만 생각해 내가 찾은 단어가 몇번째 인덱스에서 끝나는지 찾고, 인덱스+1이 샵이라면 포함해서 비교하고 아니라면 기존인덱스까지 찾아 비교
# 조건이 일치하는 음악이 여러개 일 때 -> 재생시간이 긴 순서
# 재생시간이 같은 경우 -> 먼저 입력된 음악 순서
# 입력 정렬을 1. 재생시간이 긴 순서 2. 먼저 입력된 순서로 변경

            
    return answer