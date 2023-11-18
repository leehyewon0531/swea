import sys
sys.stdin = open('input.txt', 'r')

def dfs(idx, taste_sum, kal_sum):
    global maxValue

    if kal_sum > L:
        return

    if idx == N:
        if maxValue < taste_sum:
            maxValue = taste_sum
        return

    if maxValue < taste_sum:
        maxValue = taste_sum

    dfs(idx + 1, taste_sum + arr[idx][0], kal_sum + arr[idx][1])
    dfs(idx + 1, taste_sum, kal_sum)


T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    arr = []
    maxValue = 0

    for i in range(N):
        arr.append(list(map(int, input().split())))

    dfs(0, 0, 0)
    print('#{} {}'.format(tc, maxValue))