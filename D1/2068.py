import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  li = list(map(int, input().split()))
  max = -1
  for i in li:
    if (i > max):
      max = i
  print('#{} {}'.format(tc, max))