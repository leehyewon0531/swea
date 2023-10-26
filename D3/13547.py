import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    s = input()
    print('#{} {}'.format(tc, 'YES' if s.count('x') <= 7 else 'NO'))