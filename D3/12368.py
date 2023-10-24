import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    [A, B] = list(map(int, input().split()))
    sum = A + B
    while(sum // 24 > 0):
        sum %= 24
    print('#{} {}'.format(tc, sum))