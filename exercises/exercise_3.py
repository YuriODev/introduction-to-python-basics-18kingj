# Exercise 3
seconds = int(input("Enter the time in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60
print(f"{hours}:{minutes}:{seconds}")