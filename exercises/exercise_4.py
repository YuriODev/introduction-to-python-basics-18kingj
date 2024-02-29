# Exercise 4
num = input()
if len(num) != 4:
  print(0)
elif num[0] == num[3] and num[1] == num[2]:
  print(1)
else:
  print(0)