import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, list(input().split())[0]))
    init = [0 for i in range(len(arr))]
    cnt = 0

    for i in range(len(arr)):
        if arr[i] != init[i]:
            init[i:] = [0] * (len(init) - i) if init[i] == 1 else [1] * (len(init) - i)
            cnt += 1

    print('#{} {}'.format(tc, cnt))