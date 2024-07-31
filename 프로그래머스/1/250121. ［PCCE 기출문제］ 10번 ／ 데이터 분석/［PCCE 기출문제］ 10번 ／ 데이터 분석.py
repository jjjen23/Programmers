dict = {
    "code" : 0,
    "date" : 1,
    "maximum" : 2,
    "remain" : 3
}
def solution(data, ext, val_ext, sort_by):
    ext = dict[ext]
    sort_by = dict[sort_by]
    
    answer = []
    
    for row in data:
        if row[ext] < val_ext:
            answer.append(row)
    
    answer.sort(key=lambda x : x[sort_by])
    
    return answer