import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  num = int(input())
  temp_num = num
  res = set()
  i = 1

  while(len(res) < 10):
    for val in str(temp_num):
        res.add(int(val))

    i += 1
    temp_num = num * i

  print('#{} {}'.format(tc, num * (i - 1)))