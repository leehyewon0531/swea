import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
res = ""
arr = ['3', '6', '9']
for i in range(1, T+1):
  cnt = 0
  for a in arr:
      cnt += str(i).count(a)
  if(cnt == 0):
    res += "{} ".format(str(i))
  else:
    temp = "-" * cnt
    res += "{} ".format(temp)
print(res[:-1])