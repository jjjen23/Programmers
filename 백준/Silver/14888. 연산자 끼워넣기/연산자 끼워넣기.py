n = int(input())
aList = list(map(int, input().split()))
operList = list(map(int, input().split()))  # +, -, *, / 개수

max_val = -int(1e9)
min_val = int(1e9)


def dfs(idx, total, plus, minus, mul, div):
    global max_val, min_val

    if idx == n:
        max_val = max(max_val, total)
        min_val = min(min_val, total)
        return

    if plus:
        dfs(idx+1, total+aList[idx], plus-1, minus, mul, div)
    if minus:
        dfs(idx+1, total-aList[idx], plus, minus-1, mul, div)
    if mul:
        dfs(idx + 1, total * aList[idx], plus, minus, mul-1, div)
    if div:
        if total < 0:
            dfs(idx + 1, -(-total // aList[idx]), plus, minus, mul, div-1)

        else:
            dfs(idx + 1, total // aList[idx], plus, minus, mul, div-1)

dfs(1,aList[0],operList[0],operList[1],operList[2],operList[3])

print(max_val)
print(min_val)