import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  res = 1
  num = int(input())
  if (num == 1):
    print('#{} {}'.format(tc, res))
  else:
    for i in range(2, num+1):
      if(i % 2 == 0):
        res -= i
      else:
        res += i
    print('#{} {}'.format(tc, res))