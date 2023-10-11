import sys
sys.stdin = open('input.txt', 'r')

tc = list(input().upper())
str = ''

for el in tc:
  str = str + ' {}'.format(ord(el) - 64)

print(str[1:])