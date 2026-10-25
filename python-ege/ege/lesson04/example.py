from itertools import product
codes = ["0", "10"]
for length in range(1,6):
    found = []
    for chars in product("01", repeat=length):
        word = "".join(chars)
        if all(not word.startswith(c) and not c.startswith(word) for c in codes):
            found.append(word)
    if found:
        print(found)
        break
