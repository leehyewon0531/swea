import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    students = int(input())
    print('#{} {}'.format(tc, students // 3))