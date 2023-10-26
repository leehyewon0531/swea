import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    input_list = list(input())
    res = "Yes"
    arr = []
    for el in input_list:
        if(el not in arr):
            arr.append(el)

    if len(arr) != 2:
        res = "No"

    for a in arr:
        if(input_list.count(a) != 2):
            res = "No"
            break

    print('#{} {}'.format(tc, res))