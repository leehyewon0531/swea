import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    res = 0
    standard = N // 2
    for a in range(N):
        temp = list(map(int, input().split()[0]))
        arr.append(temp)

    for i in range(N):
        for j in range(N):
            if i <= standard:
                if (standard - i) <= j <= (standard + i):
                    res += arr[i][j]
            else:
                if (standard - (N - i - 1)) <= j <= (standard + (N - i - 1)):
                    res += arr[i][j]

    print('#{} {}'.format(tc, res))