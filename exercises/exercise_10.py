# Exercise 10
hour_angle = int(input("Enter the hour angle: "))
hour = hour_angle % 30
minute_angle = hour * 12
print(minute_angle)