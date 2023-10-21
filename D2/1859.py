import sys
sys.stdin = open('input.txt', 'r')

# 어차피 물건은 뒤에 나오는 금액이 가장 큰 날에 판매하기 때문에 뒤에서부터 계산

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    arr = list(map(int, input().split()))
    res = 0

    max = arr[-1]
    for idx in range(num - 1, -1, -1):
        if arr[idx] >= max:
            max = arr[idx]
        else:
            res += max - arr[idx]

    print('#{} {}'.format(tc, res))