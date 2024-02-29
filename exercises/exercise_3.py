# Exercise 3
seconds = int(input("Enter the time in seconds: "))
hours = (seconds // 3600) % 24
minutes = (seconds // 60) % 60
seconds = seconds % 60
print(f"{hours}:{minutes:02d}:{seconds:02d}")