# Exercise 11
cost = int(input())
five_hun = 0
while cost >= 500:
  five_hun = five_hun + 1
  cost = cost - 500
one_hun = 0
while cost >= 100:
  one_hun = one_hun + 1
  cost = cost - 100
ten = 0
while cost >= 10:
  ten = ten + 1
  cost = cost - 10
five = 0
while cost >= 5:
  five = five + 1
  cost = cost - 5
one = 0
while cost >= 1:
  one = one + 1
  cost = cost - 1
print(f" {five_hun}(500), {one_hun}(100), {ten}(10), {five}(5), {one}(1)")