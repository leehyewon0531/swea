import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    length = int(input())
    input_str = input()

    if length == 1:
        print('#{} {}'.format(tc, "No"))
        continue

    strA = input_str[0:length//2]
    strB = input_str[length//2:]

    if strA == strB:
        print('#{} {}'.format(tc, "Yes"))
    else:
        print('#{} {}'.format(tc, "No"))