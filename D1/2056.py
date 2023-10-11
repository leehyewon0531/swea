import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T+1):
  line = input()
  y = line[0:4]
  m = line[4:6]
  d = line[6:]
  if((int(m) >= 1) and (int(m) <= 12)):
    if((int(d) >= 0) and (int(d) <= days[int(m)])):
      print('#{} {}/{}/{}'.format(tc, y, m, d))
      continue
  print('#{} -1'.format(tc))