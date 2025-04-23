# 캠핑 # 브론즈 # 그리디
# 캠핑장을 연속하는 p일 중, L일동안만 사용할 수 있다.
# v일짜리 휴가를 시작했을때 캠핑장을 최대 며칠동안 사용할 수 있는 가?

i = 1

while True:
    answer = 0
    l,p,v = map(int, input().split())
    if l == 0 and p==0 and v == 0:
        break
    else:
        answer += ((v // p) * l) + min(v%p , l)
        print(f"Case {i}: {answer}")
        i+=1

