import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  res = 1
  str = list(input())
  for i in range(len(str) // 2):
    if(str[i] != str[len(str) - i - 1]):
      res = 0
  print('#{} {}'.format(tc, res))