import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    min = num + 1

    for i in range(1, int(num ** (1 / 2)) + 1):
        if(num % i == 0):
            if(min > (i + (num // i))):
                min = i + (num // i)

    print('#{} {}'.format(tc, min - 2))