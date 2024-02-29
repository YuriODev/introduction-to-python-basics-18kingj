# Exercise 8
a = int(input()
b = int(input())
c = int(input())

min = min(a, b, c)
max = max(a, b, c)
mid = a + b + c - min - max
print(min)
print(mid)
print(max)