import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]
def dfs(x, y, idx, count):
    global result
    if count >= 5:
        result = "YES"
        return

    nx = x + dx[idx]
    ny = y + dy[idx]

    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        return

    if arr[nx][ny] == 'o':
        dfs(nx, ny, idx, count + 1)
    else:
        return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    result = "NO"

    for i in range(N):
        arr.append(list(input().split()[0]))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                for d in range(8):
                    dfs(i, j, d, 1)
            if result == "YES":
                break

    print('#{} {}'.format(tc, result))