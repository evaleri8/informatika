bits = 45 * 22050 * 16 * 2
unit = 8 * 1024
print((bits + unit - 1) // unit)
