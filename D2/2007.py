import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  str = input() 
  key = str[0] 
  for idx in range(1, 30):
    i = 0
    while(i < len(key)):
      if(str[idx + i] == key[i]):
        i += 1
      else:
        break
    if(i == len(key)):
      break
    else:
      key += str[idx]
  print('#{} {}'.format(tc, len(key)))