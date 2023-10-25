import sys
sys.stdin = open('input.txt', 'r')

# 바로 이전 문자와 비교해야 하는 경우에는 stack을 활용하자

for tc in range(1, 11):
    [N, pwd] = list(map(int, input().split()))
    li = list(str(pwd))
    stack = []

    for i in range(len(li)):
        # stack[len(stack)-1]은 stack[-1]로 개선할 수 있다!!
        if(len(stack) > 0 and stack[len(stack) - 1] == li[i]):
            stack.pop()
        else:
            stack.append(li[i])

    print('#{} {}'.format(tc, int(''.join(stack))))
