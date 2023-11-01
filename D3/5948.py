import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    num_arr = list(map(int, input().split()))
    res_set = set()

    for i in range(0, len(num_arr) - 2):
        for j in range(i + 1, len(num_arr) - 1):
            for k in range(j + 1, len(num_arr)):
                res_set.add(num_arr[i] + num_arr[j] + num_arr[k])

    sorted_set = sorted(res_set)
    print('#{} {}'.format(tc, sorted_set[len(sorted_set) - 5]))
