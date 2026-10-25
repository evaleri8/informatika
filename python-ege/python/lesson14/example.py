from itertools import product
count = 0
for letters in product("ABC", repeat=3):
    word = "".join(letters)
    if word.count("A") == 1:
        count += 1
print(count)
