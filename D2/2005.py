import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
  num = int(input())
  print("#{}".format(tc))
  for i in range(num):
    if(i == 0):
      print("1")
    elif(i == 1):
      print("1 1")
    else:
      str = "1"
      for j in range(i - 1):
        str += " {}".format(i)
      str += " 1"
      print(str)