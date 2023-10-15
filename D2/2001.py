import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  [N, M] = list(map(int, input().split()))
  arr = []
  res = 0
  for a in range(0, N):
    li = list(map(int, input().split()))
    arr.append(li)
  for i in range(N - M + 1):
    for j in range(N - M + 1):
      sum = 0
      for k in range(M):
        for l in range(M):
          sum += arr[i+k][j+l]
      if sum > res:
        res = sum
  print('#{} {}'.format(tc, res))