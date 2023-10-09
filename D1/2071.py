import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
  sum = 0
  li = list(map(int, input().split()))
  for i in li:
    sum += i
  print("#{} {}".format(test_case, round(sum / len(li))))