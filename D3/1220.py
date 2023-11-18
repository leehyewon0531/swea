import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = []
    cnt = 0
    for a in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                for k in range(i, N):
                    if i+1 < N:
                        if arr[i+1][j] == 0:
                            arr[i][j] = 0
                            arr[i+1][j] = 1
                        else:
                            break
            elif arr[i][j] == 2:
                for k in range(i, 0, -1):
                    if i-1 >= 0:
                        if arr[i-1][j] == 0:
                            arr[i][j] = 0
                            arr[i-1][j] = 2
                        else:
                            break
            else:
                continue

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if i+1 < N and arr[i+1][j] == 2:
                    cnt += 1

    print('#{} {}'.format(tc, cnt))
