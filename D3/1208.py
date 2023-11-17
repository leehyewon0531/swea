import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    dump_cnt = int(input())
    arr = list(map(int, input().split()))
    i = 0

    while(i < dump_cnt):
        arr.sort()
        arr[0] = arr[0] + 1
        arr[99] = arr[99] - 1
        i += 1

    arr.sort()
    print('#{} {}'.format(tc, arr[99] - arr[0]))