import sys
sys.stdin = open('input.txt', 'r')

def dfs(idx, sum):
    global count

    if sum == K:
        count += 1
        return

    if sum > K:
        return

    if idx == N:
        if sum == K:
            count += 1
        return

    dfs(idx + 1, sum + arr[idx])
    dfs(idx + 1, sum)
    return

T = int(input())

for tc in range(1, T+1):
    [N, K] = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    count = 0

    dfs(0, 0)
    print('#{} {}'.format(tc, count))