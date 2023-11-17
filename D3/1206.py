import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    arr = [[0 for a in range(255)] for b in range(N)]
    cnt = 0

    for i in range(2, len(heights) - 1):
        arr[i][0:heights[i]] = [1] * heights[i]

    for i in range(N):
        for j in range(255):
            if arr[i][j] == 1:
                if (i-2) >= 0 and (i+2) <= N:
                    if arr[i-2][j] == 0 and arr[i-1][j] == 0 and arr[i+1][j] == 0 and arr[i+2][j] == 0:
                        cnt += 1

    print('#{} {}'.format(tc, cnt))