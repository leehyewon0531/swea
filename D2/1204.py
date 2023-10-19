import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    li = list(map(int, input().split()))
    li.sort()
    res = 0
    cnt = 0
    i = 0
    while(len(li) > i):
        if(li.count(li[i]) >= cnt):
            cnt = li.count(li[i])
            res = li[i]
            i += cnt
            continue
        i += 1
    print('#{} {}'.format(tc, res))