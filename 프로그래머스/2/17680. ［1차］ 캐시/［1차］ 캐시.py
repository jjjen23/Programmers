from collections import deque

def solution(cacheSize, cities):
    answer = 0
    #d = deque([1,2,3])
    #d.rotate(-1)
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    
    cache = deque()
    
    for city in cities:
        city = city.lower()
        if len(cache) < cacheSize:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                cache.append(city)
                answer += 5
        else:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                answer += 1
            else:
                if cache:
                    cache.popleft() # 가장 참조 오래된것 pop시키기
                    cache.append(city) # 새롭게 추가시키기
                    answer += 5
    
            
    return answer

"""
    for i in range(cacheSize):
        cities[i]=cities[i].lower() # 전부 소문자로 변경해서 집어 넣기
        if cities[i] in cache:
            cache.remove(cities[i])
            cache.append(cities[i]) # 최신 참조로 교체
            answer += 1
        else:
            cache.append(cities[i])
            answer += 5
    
    for i in range(cacheSize, len(cities)):
        cities[i]=cities[i].lower()
        # hit일때
        if cities[i] in cache:
            cache.remove(cities[i])
            cache.append(cities[i]) # 최신 참조로 교체
            answer += 1
            # print(cache)
        # miss일때
        else:
            if cache:
                cache.popleft() # 가장 참조 오래된것 pop시키기
                cache.append(cities[i]) # 새롭게 추가시키기
                answer += 5
            # print(cache)
"""