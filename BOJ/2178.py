import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

# DFS -> 모든 경로 다 봐야 하는 경우
# BFS -> 최단거리, 최단횟수 찾는 경우

[N, M] = list(map(int, input().split()))
arr = []
for el in range(N):
    arr.append(list(map(int, list(input()))))

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or nx >= N or ny < 0 or ny >= M):
                continue

            if(arr[nx][ny] == 0):
                continue

            if(arr[nx][ny] == 1):
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))

    return arr[N-1][M-1]

print(bfs(0, 0))