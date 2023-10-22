import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    [P, Q, R, S, W] = list(map(int, input().split()))
    first = P * W
    second = Q if W <= R else Q + (W - R) * S

    print('#{} {}'.format(tc, first if first < second else second))