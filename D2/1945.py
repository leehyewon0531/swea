import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
result = [0 for i in range(5)]
index = [2, 3, 5, 7, 11]

for tc in range(1, T+1):
  result = [0 for i in range(5)]
  num = int(input())
  for idx in range(len(index)):
    while(num % index[idx] == 0):
      num = num // index[idx]
      result[idx] = result[idx] + 1
  print('#{} {}'.format(tc, ' '.join(str(_) for _ in result)))