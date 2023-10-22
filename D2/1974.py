import sys
sys.stdin = open('input.txt', 'r')

# 가로줄, 세로줄 유효성 검사
# x, y가 둘 다 3으로 나누어 떨어지면(0, 3, 6) 3x3 유효성 검사

T = int(input())
def checkDuplication(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if(arr[i] == arr[j]):
                return False
    return True

for tc in range(1, T+1):
    sudoku = []
    res = 1
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    for a in range(9):
        # 여기서 row, column 넣어서 checkDuplication 호출
        if (not checkDuplication(sudoku[a])):
            res = 0
            break
        if(not checkDuplication([sudoku[i][a] for i in range(9)])):
            res = 0
            break
        for b in range(9):
            # 여기서 3x3 넣어서 checkDuplication 호출
            if (a % 3 == 0) and (b % 3 == 0):
                temp_list = []
                for i in range(3):
                    for j in range(3):
                        temp_list.append(sudoku[a + i][b + j])
                if(not checkDuplication(temp_list)):
                    res = 0
                    break

    print('#{} {}'.format(tc, res))