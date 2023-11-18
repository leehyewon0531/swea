import sys
sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    queue = list(map(int, input().split()))
    flag = True

    while flag:
        for i in range(1, 6):
            temp = queue.pop(0)
            if temp - i <= 0:
                temp = 0
                queue.append(temp)
                flag = False
                break
            else:
                temp = temp - i
                queue.append(temp)

    result = ' '.join([str(_) for _ in queue])
    print('#{} {}'.format(tc, result))