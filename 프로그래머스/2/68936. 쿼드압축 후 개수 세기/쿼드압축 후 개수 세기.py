def comp(arr,x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != arr[x][y]:
                n //= 2 # 분할
                # 사분할하여 재귀
                comp(arr,x,y,n)
                comp(arr,x+n,y,n)
                comp(arr,x,y+n,n)
                comp(arr,x+n,y+n,n)
                return
    # 값이 모두 같으면
    answer[arr[i][j]] += 1

def solution(arr):
    global answer
    answer = [0,0]
    length = len(arr)
    comp(arr,0,0,length)
         
            
    return answer
