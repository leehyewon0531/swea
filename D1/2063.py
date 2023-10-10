import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
li = list(map(int, input().split()))
li.sort()
print(li[T//2])