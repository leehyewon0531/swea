import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    [N, Q] = list(map(int, input().split()))
    arr = [0 for _ in range(N)]

    for idx in range(Q):
        [L, R] = list(map(int, input().split()))

        for i in range(L - 1, R):
            arr[i] = idx + 1

    res = ' '.join(str(_) for _ in arr)
    print('#{} {}'.format(tc, res))
