import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  li = list(map(int, input().split()))
  li.sort()
  sum = 0
  for i in range(1, len(li) - 1):
    sum += li[i]
  print('#{} {}'.format(tc, round(sum / 8)))