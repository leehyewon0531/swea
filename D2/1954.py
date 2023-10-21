import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    arr = [[0 for _ in range(num)] for _ in range(num)]
    i = 1
    [x, y] = [0, 0]
    arr[x][y] = i

    while(i < num * num):
        while True:
            if(y + 1 >= num or arr[x][y+1] != 0):
                break
            else:
                i += 1
                arr[x][y+1] = i
                y += 1

        while True:
            if(x + 1 >= num or arr[x+1][y] != 0):
                break
            else:
                i += 1
                arr[x+1][y] = i
                x += 1

        while True:
            if(y - 1 < 0 or arr[x][y-1] != 0):
                break
            else:
                i += 1
                arr[x][y-1] = i
                y -= 1

        while True:
            if(x - 1 < 0 or arr[x-1][y] != 0):
                break
            else:
                i += 1
                arr[x-1][y] = i
                x -= 1
    print('#' + str(tc))
    for n in range(num):
        temp_str = ' '.join(str(_) for _ in arr[n])
        print(temp_str)