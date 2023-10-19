import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  num = int(input())
  li = list(map(int, input().split()))
  li.sort()
  s = ' '.join(str(_) for _ in li)
  print('#{} {}'.format(tc, s))