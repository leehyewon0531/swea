import sys
sys.stdin = open('input.txt', 'r')

# 한 줄로만 쭉 전개되는 걸 생각하자 ㅠ.ㅠ...

T = int(input())
for tc in range(1, T+1):
  [N, K] = list(map(int, input().split()))
  arr = []
  for i in range(N):
    li = list(map(int, input().split()))
    arr.append(li)
  
  result = 0
  # 행 확인
  for i in range(N) :
      cnt = 0
      for j in range(N) :
          if arr[i][j] == 1 :
              cnt += 1
          if arr[i][j] == 0 or j == N - 1 :
              if cnt == K :
                  result += 1
              if arr[i][j] == 0 :
                  cnt = 0

  # 열 확인
  for i in range(N) :
      cnt = 0
      for j in range(N) :
          if arr[j][i] == 1 :
              cnt += 1
          if arr[j][i] == 0 or j == N - 1 :
              if cnt == K :
                  result += 1
              if arr[j][i] == 0 :
                  cnt = 0

  print('#{} {}'.format(tc, result))