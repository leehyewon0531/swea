import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T+1):
  [N, K] = list(map(int, input().split()))
  K -= 1
  K_score = 0
  arr = []
  for i in range(N):
    li = list(map(int, input().split()))
    arr.append(li[0] * 0.35 + li[1] * 0.45 + li[2] * 0.2)
  K_score = arr[K]
  arr.sort()
  arr.reverse()

  for j in range(N):
    if(arr[j] == K_score):
      print('#{} {}'.format(tc, grade[(j * 10) // N]))