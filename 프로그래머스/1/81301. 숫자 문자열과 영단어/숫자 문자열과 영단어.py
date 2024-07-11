dict = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}

def solution(s):
    answer = 0
    for str in dict:
        # s 문장에서 str을 dict[str]로 대체
        s = s.replace(str, dict[str])
    answer = int(s)
    return answer