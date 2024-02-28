# Exercise 1
list = input("Enter a list of numbers: ")
first_num = 0
second_num = 0
for i in range(5):
  if i == 1 or i == 3:
    second_num = second_num + int(list[i])
  else:
    first_num = first_num + int(list[i])
final_num = str(first_num) + str(second_num)
print(final_num)