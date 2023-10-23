import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    [L, U, X] = list(map(int, input().split()))
    if(X < L):
        print('#{} {}'.format(tc, L - X))
        continue
    if(X > U):
        print('#{} {}'.format(tc, -1))
        continue
    print('#{} {}'.format(tc, 0))