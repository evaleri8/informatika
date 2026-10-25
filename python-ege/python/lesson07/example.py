n = 87
x = n
s = ""
if x == 0:
    s = "0"
while x > 0:
    s = str(x % 5) + s
    x //= 5
print(s)
print(int(s, 5))
