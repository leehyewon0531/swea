import sys
sys.stdin = open('input.txt', 'r')

arr = [1, 2, 3, 1]
[A, B] = list(map(int, input().split()))

for el in range(len(arr)):
  if(A == arr[el]):
    if(B == arr[el + 1]):
      print('B')
    else:
      print('A')
    break