import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
  li = list(map(int, input().split()))
  if li[0] < li[1]:
    print('#{} {}'.format(test_case, '<'))
  elif li[0] > li[1]:
    print('#{} {}'.format(test_case, '>'))
  else:
    print('#{} {}'.format(test_case, '='))